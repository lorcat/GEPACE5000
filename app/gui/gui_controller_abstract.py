__author__ = "Konstantin Glazyrin"
# main common libraries
from app.load import *

# specific libraries
from app.load.load_config import *
from app.load.load_runnables import *

from app.pytango import write_attribute_asynch, command_inout, change_attribute_by_step

class AbstractController(Tester):
    SETPOINT_MIN = 0.
    SETPOINT_MAX = 200.
    SETPOINT_DELIM = 2
    SETPOINT_STEP_DEFAULT = 1.

    SLEWRATE_MIN = 0.01
    SLEWRATE_MAX = 200.
    SLEWRATE_STEP_DEFAULT = 1.
    SLEWRATE_DELIM = 4

    # values for tango attributes to control
    PRESSURECONTROL_ON = 1
    PRESSURECONTROL_OFF = 0

    OVERSHOOT_ON = 1
    OVERSHOOT_OFF = 0

    SLEWRATEMODE_MAX = 1
    SLEWRATEMODE_LIN = 0

    CMD_DECOMPRESS = "Decompress"

    # lists of values to regulate slew rate and steps
    SLEWRATE_STEPS = [0.1, 0.25, 0.33, 0.5, 1, 1.5, 2, 3, 4, 5, 6, 10, 20, 30, 40, 50, 100]
    SETPOINT_STEPS = [0.1, 0.25, 0.5, 1, 2, 3, 4, 5, 10, 20, 30]

    SETPOINTS_POINTS = [0, 1, 2, 4, 5, 6, 8, 10, 15, 20, 25, 30, 45]

    def __init__(self, main_wnd, parent=None):
        Tester.__init__(self)

        # reference to the main window
        self.main_wnd = main_wnd

        # pool to run single task workers
        self.thread_pool = getPool()

        # list with dictionaries setting a relation  - widget; attr; value
        self.widget_list = {}

        self.tango_device = config.PROFILES[PROFILE_START][PROFILE_TANGO_ADDRESS]


    def runCommand(self, cmd, arg=None):
        """
        Prepares a separate worker thread running a command
        :return:
        """
        self.debug("Running a command with argument ({}, {})".format(cmd, arg))

        if self.test(arg):
            func = lambda d=self.tango_device, c=cmd, a=arg: command_inout(d, c, arg)
            runner = LambdaRunner(func)
            self.thread_pool.tryStart(runner)
        else:
            func = lambda d=self.tango_device, c=cmd: command_inout(d, c)
            runner = LambdaRunner(func)
            self.thread_pool.tryStart(runner)


    def writeAttribute(self, attr, value):
        """
        Prepares a separate worker intended for a remote
        :param attr:
        :param value:
        :return:
        """
        self.debug("Writing an attribute value ({}, {})".format(attr, value))

        func = lambda d=self.tango_device, a=attr, v=value: write_attribute_asynch(d, a, v)
        runner = LambdaRunner(func)
        self.thread_pool.tryStart(runner)

    def readAndChangeAttribute(self, attr, step):
        """
        Prepares a separate worker intended for a remote
        :param attr:
        :param value:
        :return:
        """
        self.debug("Changing an attribute value by a step ({}, {})".format(attr, step))


        func = lambda d=self.tango_device, a=attr, s=step: change_attribute_by_step(d, a, s)
        runner = LambdaRunner(func)
        self.thread_pool.tryStart(runner)

    def processAttributes(self, data):
        """
        Processes an attribute update event and applies new values to the status fields if needed
        :param data:
        :return:
        """
        ref_data = deepcopy(data)
        self.debug("Processing the new data ({})".format(ref_data))

        # process only viable data
        if len(ref_data) > 0:
            for (i, el) in enumerate(ref_data):
                self.debug("Processing element data ({})".format(el))
                key = None
                try:
                    key = DATA
                    value = el[key]
                    key = DATASTR
                    datastr = el[key]
                    key = ATTR
                    attr = el[ATTR]

                    # operate with the proper attributes
                    if self.widget_list.has_key(attr):
                        self.widget_list[attr][WDGT].setText(datastr)
                        self.widget_list[attr][DATASTR] = datastr
                        self.widget_list[attr][DATA] = value
                except AttributeError:
                    self.error("Error on processing new data, no key ({})".format(key))

            del ref_data[:]

    def addWdgtDblValidator(self, wdt, mi, ma, decim=2):
        """
        Set-ups a validator for a specific widget
        :return:
        """
        self.debug("Setting a double validator for a widget ({}, min: {}, max: {})".format(wdt, mi, ma))
        val = qtgui.QDoubleValidator(mi, ma, decim, parent=wdt)
        val.setDecimals(decim)
        val.setNotation(qtgui.QDoubleValidator.ScientificNotation)
        wdt.setValidator(val)

    def setWdgtDefaultValue(self, wdgt, value):
        """
        Sets a default value to the widget in case it is empty
        :param value:
        :return:
        """
        wdgt.setText(str(value))

    def checkWdgtValidator(self, wdgt):
        """
        Performes a test on a widget validator
        :param wdgt:
        :return:
        """
        if wdgt.validator().validate(wdgt.text(), 0) == qtgui.QValidator.Invalid:
            raise ValueError


    def changeValueByStep(self, attr, wdgt_step, mi_test, ma_test, sign=1):
        """
        Changes a value by a step
        :param attr: attribute to check
        :param wdgt_step: step widget to check
        :param mi_test: min value to take into account
        :param ma_test: max value to take into account
        :return:
        """
        key = None
        try:
            self.checkWdgtValidator(wdgt_step)

            # ok - sending the value to the device
            step = float(wdgt_step.text())

            key = DATA
            value = float(self.widget_list[attr][key])

            # test for the range
            if value + sign*step < mi_test or value + sign*step > ma_test:
                return

            # adjust for the bar/sec parameters
            if attr == SLEWRATE or attr == DECOMPRESSRATE:
                step = float(step / 60.)

            # pass values to the tango runner
            self.readAndChangeAttribute(attr, sign*step)

        except ValueError:
            msg = "Wrong parameter for step value"
            qtgui.QMessageBox.critical(self.main_wnd, "Error", msg)
            self.error(msg)
        except AttributeError:
            self.error("No information on the key ({})".format(key))

    def actionStopControl(self):
        """
        Stops the pump control
        :return:
        """
        self.debug("Stopping the pump control")

        self.writeAttribute(PRESSURECONTROL, self.PRESSURECONTROL_OFF)

    def createCustomContextMenu(self, *args):
        """
        Creates a custom context menu for certain widgets
        :param args:
        :return:
        """
        self.debug("Creating a custom context menu ({})".format(args))

        event = args[0]
        attr, wdgt = args[2][0], args[2][1]

        menu = qtgui.QMenu()

        menu_items = []

        if attr == SLEWRATE or attr == DECOMPRESSRATE:
            menu_items = self.SLEWRATE_STEPS
        elif attr == SETPOINT:
            menu_items = self.SETPOINT_STEPS
        else:
            menu_items = self.SETPOINTS_POINTS

        if len(menu_items):
            for (i, el) in enumerate(menu_items):
                form = "{}"
                if el < 1:
                    form = "{:1.2f}"
                value = form.format(el)

                act = qtgui.QAction(menu)
                act.setText(value)
                menu.addAction(act)
            res_act = menu.exec_(wdgt.mapToGlobal(event.pos()))

            # apply the value to the widget of interest
            if self.test(res_act):
                wdgt.setText(res_act.text())
