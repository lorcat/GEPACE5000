__author__ = 'Konstantin Glazyrin'

from app.load import *
from app.load.load_config import *

from app.config.keys import *
from app.config import configuration as config

from app.pytango import *

# object controlling thread for reader
class ReaderController(qtcore.QObject, Tester):
    DEFAULT_PRIORITY = qtcore.QThread.InheritPriority
    DEFAULT_THREAD_TIMEOUT = 3000

    # proxy for new data signal
    sign_newdata = qtcore.pyqtSignal(object)

    def __init__(self, parent=None):
        qtcore.QObject.__init__(self, parent=parent)
        Tester.__init__(self)

        # thread
        self._runner = qtcore.QThread(parent=self)

        # object to run in the thread
        self._reader = Reader()

        # timer controlling the reader
        self._timer = qtcore.QTimer(parent=self)

        # init main events
        self.__init_events()

        # init thread
        self.__init_thread()

    def __init_events(self):
        """
        Initializes events related to the operation
        :return:
        """
        self.debug("Initializing signals")

        # timer signal
        self.connect(self._timer, qtcore.SIGNAL("timeout()"), self._reader.run)

        # thread signals
        self.connect(self._runner, qtcore.SIGNAL("started()"), self.processThreadStart)
        self.connect(self._runner, qtcore.SIGNAL("finished()"), self.processThreadFinish)

        # reader signals - new data loop
        self._reader.registerNewData(self.reportNewData)

        # set interval and timer type
        self._timer.setSingleShot(False)
        try:
            self._timer.setInterval(config.PROFILES[PROFILE_START][PROFILE_DELAY])
        except KeyError:
            self.error("Configuration error on profile (keys: {}|{})".format(PROFILE_START, PROFILE_DELAY))

    def __init_thread(self):
        """
        Initializes thread
        :return:
        """
        self.debug("Initializing thread")

        priority = self.DEFAULT_PRIORITY
        try:
            priority = config.PROFILES[PROFILE_PRIORITY]
        except KeyError:
            self.error("Configuration error on profile (keys: {})".format(PROFILE_PRIORITY))
            self.error("Using default priority ({})".format(priority))

        self._runner.start(priority)

        # move to the different thread
        self._reader.moveToThread(self._runner)

    def cleanup(self):
        """
        Stops thread operation, moves object to the main thread
        :return:
        """
        # stop timer
        self.stopReader()

        # delete object
        self._reader.deleteLater()

        # delete thread
        if self._runner.isRunning():
            self._runner.terminate()
            self._runner.wait(self.DEFAULT_THREAD_TIMEOUT)

    def processThreadStart(self):
        self.debug("Reading Thread has started")

    def processThreadFinish(self):
        self.debug("Reading Thread has finished")

    def registerNewData(self, func):
        """
        Registers function to be fired on the new data - proxy
        :return:
        """
        self.debug("Registering signal with func ({})".format(func))
        self.sign_newdata.connect(func)

    def reportNewData(self, data):
        """
        Reports new data via Qt signal
        :param data:
        :return:
        """

        self.debug("Reporting new data ({}) by reader".format(str(data)))
        self.sign_newdata.emit(data)

    @qtcore.pyqtSlot()
    def startReader(self):
        """
        Starts the timer engaging the reader
        :return:
        """
        self._timer.start()
        self.debug("{}".format(self._timer.isActive()))

    @qtcore.pyqtSlot()
    def stopReader(self):
        """
        Stops the timer engaging the reader
        :return:
        """
        self._timer.stop()


# object which runs the reading operation
class Reader(qtcore.QObject, Tester):
    # mutex timeout in ms
    MUTEX_TIMEOUT = 100

    DATA = {}

    # signal emitted at the end of the read loop
    sign_newread = qtcore.pyqtSignal(object)

    def __init__(self, parent=None):
        qtcore.QObject.__init__(self, parent=parent)
        Tester.__init__(self)

        # mutex used to test the permission for the action start
        self._access_mutex = qtcore.QMutex()

    def run(self):
        """
        Function to be run on the
        :return:
        """

        self.info("Starting reading action")

        # try mutex lock - if not posible return
        btest = self.tryLock()

        if btest:
            self.info("Obtained lock - reading operation has started")

            # read data
            self.read()

            # don't forget to unlock the mutex
            self.unlock()
        else:
            self.info("Lock was not obtained - try to adjust the polling period.")
        return

    def unlock(self):
        """
        Unlocks mutex controlling reading operation
        :return:
        """
        self._access_mutex.unlock()

    def tryLock(self):
        """
        Trying to set a lock to start reading operation
        :return:
        """
        return self._access_mutex.tryLock(self.MUTEX_TIMEOUT)

    def read(self):
        """
        Reads data and returns it
        :return:
        """
        # storage for data
        data = []

        # get cmdloop
        loop = None
        try:
            loop = config.PROFILES[PROFILE_START][PROFILE_ATTRLOOP]
        except KeyError:
            self.error("Configuration error on profile (keys: {}, {})".format(PROFILE_START, PROFILE_ATTRLOOP))
            return

        device_path, device = None, None
        try:
            device_path = config.PROFILES[PROFILE_START][PROFILE_TANGO_ADDRESS]
        except KeyError:
            pass

        if self.test(device_path):
            device = CustomProxy(device_path)

        # process unless an error was reported
        bupdated, num_udated = False, 0
        berror = device.isError()

        # create a timestamp
        lt = time.localtime()
        date = "{:04}-{:02}-{:02}_{:02}:{:02}:{:02}".format(lt.tm_year, lt.tm_mon, lt.tm_mday, lt.tm_hour,
                                                            lt.tm_min, lt.tm_sec)

        if not berror:
            # go through attributes - execute one by one, save return values if needed
            for (i, el) in enumerate(loop):
                self.debug("{}: {}".format(i, el))
                # get data attr
                attr = None
                try:
                    attr = el[ATTR]
                except KeyError:
                    pass
                self.debug("Processing loop event for attribute ({} : {})".format(i, attr))

                # get data desc
                desc = ""
                try:
                    desc = el[DESC]
                except KeyError:
                    pass

                self.debug("Processing loop event for description ({} with desc. {})".format(i, desc))

                # read with an expected DeviceProxy
                response = read_attribute(device_path, attr, device=device)

                # if we get useful data:
                if self.test(response):
                    # data requires saving - if nick is given and if the value is not None
                    if self.test(response[1]):
                        # convert bool to int
                        if self.test(response[1], bool):
                            response[1] = int(response[1])

                        # convert values on the fly if needed
                        # pressure control
                        if attr == PRESSURECONTROL:
                            if response[1] == 1:
                                value_str = "Running"
                            else:
                                value_str = "Idle"
                        # overshoot
                        elif attr == OVERSHOOT:
                            if response[1] == 1:
                                value_str = "ON"
                            else:
                                value_str = "OFF"
                        elif attr == SLEWRATEMODE:
                            if response[1] == 1:
                                value_str = "Maximum"
                            else:
                                value_str = "Linear"
                        else:
                            # convert values from bar/s to bar/min
                            if attr == SLEWRATE:
                                try:
                                    response[1] = float(response[1]) * 60
                                except ValueError:
                                    response[1] = -1
                            elif attr == DECOMPRESSRATE:
                                try:
                                    response[1] = float(response[1]) * 60
                                except ValueError:
                                    response[1] = -1

                            # save as string for JS or any other handling
                            try:
                                form = el[FORMAT]
                            except KeyError:
                                form = "{}"

                            # string value
                            self.debug("Using formating ({})".format(form))
                            value_str = form.format(response[1]).strip()

                        # save data
                        # check if the data was updated or not
                        if self.DATA.has_key(attr):
                            if self.DATA[attr] != value_str:
                                num_udated += 1
                                bupdated = True
                        else:
                            num_udated += 1
                            bupdated = True

                        if bupdated:
                            self.DATA[attr] = value_str
                            data.append({ATTR: attr, DATA: response[1], DESC: desc, DATASTR: value_str, TIMESTAMP: date})
                            self.debug("Appending data ({})".format(data[-1]))
                else:
                    # incomplete data indicates an error on the network
                    self.debug("Response is None, possible network issue, will repeat again")
                    berror = True
                    break

        # report data all data at once
        # empty data indicates an error
        if bupdated and len(data) > 0:
            self.reportNewData(data)
        elif berror:
            data.append({ATTR: PRESSURECONTROL, DATA: -1, DESC: "", DATASTR: "Error", TIMESTAMP: date})
            self.reportNewData(data)
        del data[:]

    def registerNewData(self, func):
        """
        Register the function to be fired on new data
        :param func:
        :return:
        """
        self.debug("Registering signal with func ({})".format(func))
        self.sign_newread.connect(func)

    def reportNewData(self, data):
        """
        Reports new data via Qt signal as a deepcopy
        :param data:
        :return:
        """
        self.debug("Reporting new data ({})".format(str(data)))
        temp = deepcopy(data)
        self.sign_newread.emit(temp)

# @TODO: report somehow the errors on unreachable devices for a person to understand
