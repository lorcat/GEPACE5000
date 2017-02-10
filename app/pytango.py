__author__ = 'Konstantin Glazyrin'

from PyTango import *

from app.load import *

# implementation of custom proxy to take care for errors and debugging messages
class CustomProxy(DeviceProxy, Tester):

    DevFailed = DevFailed
    FAULT = DevState.FAULT
    MOVING = DevState.MOVING

    def __init__(self, device_path, timeout=1):
        self.device_path = device_path

        Tester.__init__(self)

        try:
            timeout = float(timeout)
        except ValueError:
            timeout = 1

        # error state
        self._error = False
        try:
            self.debug("Initialization of the path {}".format(device_path))
            DeviceProxy.__init__(self, self.device_path)
            state = self.state()
            if state == DevState.ALARM or state == DevState.FAULT:
                raise DevFailed
        except (DevFailed, AttributeError) as e:
            self._error = True
            self.error("\nError upon the initialization ({})".format(e))
            self.debug("Initialization of device ({}) has failed ({})".format(self.device_path, self._error))

    def command_inout(self, *args, **kwargs):
        """
        Command inout overload
        """
        self.debug("command_inout ({}, {})".format(str(args), str(kwargs)))
        return DeviceProxy.command_inout(self, *args, **kwargs)

    def command_inout_asynch(self, *args, **kwargs):
        """
        Command inout asynch overload
        """
        self.debug("command_inout_asynch ({}, {})".format(str(args), str(kwargs)))
        return DeviceProxy.command_inout_asynch(self, *args, **kwargs)

    def read_attribute(self, *args, **kwargs):
        """
        read_attribute overload
        """
        self.debug("read_attribute ({}, {})".format(str(args), str(kwargs)))
        return DeviceProxy.read_attribute(self, *args, **kwargs)

    def read_attribute_asynch(self, *args, **kwargs):
        """
        read_attributes_asynch overload
        """
        self.debug("read_attribute_asynch ({}, {})".format(str(args), str(kwargs)))
        return DeviceProxy.read_attribute_asynch(self, *args, **kwargs)

    def write_attribute(self, *args, **kwargs):
        """
        write_attribute overload
        """
        self.debug("write_attribute_asynch ({}, {})".format(str(args), str(kwargs)))
        return DeviceProxy.write_attribute_asynch(self, *args, **kwargs)

    def write_attribute_asynch(self, *args, **kwargs):
        """
        write_attribute_asynch overload
        """
        self.debug("write_attribute ({}, {})".format(str(args), str(kwargs)))
        return DeviceProxy.write_attribute_asynch(self, *args, **kwargs)

    def state(self):
        """
        state() overload
        """
        res = DeviceProxy.state(self)
        self.debug("Device State is ({})".format(res))
        return res

    def report_device(self):
        """
        Outputs the path for the device
        """
        self.debug("Device: ({})".format(self.device_path))

    def debug(self, msg):
        """
        Overload of the debug function
        """
        Tester.debug(self, "{}. {}".format(self.device_path, msg))

    def error(self, msg):
        """
        Overload of the error function
        """
        Tester.error(self, "{}. {}".format(self.device_path, msg))

    def warning(self, msg):
        """
        Overload of the warning function
        """
        Tester.warning(self, "{}. {}".format(self.device_path, msg))

    def isError(self):
        """
        Returns the state of error
        :return:
        """
        return self._error

def read_attribute(device_path, attr, expected_type=float, device=None):
    """
    Reads an attribute, converts it and outputs it
    :param device_path:
    :param attr:
    :return:
    """
    res = None
    t = Tester()

    # get a working proxy or a reference
    if device is not None and isinstance(device, CustomProxy):
        d = device
    else:
        d = CustomProxy(device_path)

    if not d.isError():
        d.report_device()
        try:
            state = d.state()
            if state == DevState.FAULT or state == DevState.ALARM:
                t.error("Device has a ({}) state. Aborting the operation.".format(state))
                raise DevFailed
            else:
                res = d.read_attribute(attr).value
        except (DevFailed, AttributeError) as e:
            t.error("DevFailed upon accessing the device ()".format(d.device_path))
            return res

        t.debug("Type of attribute ({}) value is ({})".format(attr, type(res)))

        if not t.test(res):
            if expected_type is float:
                res = config.CONVERTER[DEFAULT_FLOAT]
            elif expected_type is int:
                res = int(config.CONVERTER[DEFAULT_FLOAT])
            elif expected_type is str:
                res = "NaN"

    return [d, res]

def change_attribute_by_step(device_path, attr, step, device=None):
    """
    Reads an attribute, converts it and outputs it
    :param device_path:
    :param attr:
    :return:
    """
    res = None
    t = Tester()

    # get a working proxy or a reference
    if device is not None and isinstance(device, CustomProxy):
        d = device
    else:
        d = CustomProxy(device_path)

    value = None
    if not d.isError():
        d.report_device()
        try:
            state = d.state()
            if state == DevState.FAULT or state == DevState.ALARM:
                t.error("Device has a ({}) state. Aborting the operation.".format(state))
                raise DevFailed
            else:
                value = d.read_attribute(attr).value
                value += step
                d.write_attribute_asynch(attr, value)
        except (DevFailed, AttributeError) as e:
            t.error("DevFailed upon accessing the device ()".format(d.device_path))
            return res
        except ValueError:
            t.error("Error on data conversion ()".format(value))
            return res
    return [d, res]

def write_attribute(device_path, attr, value, device=None):
    """
    Writes an attribute value
    :param device_path:
    :param attr:
    :param value:
    :return:
    """
    # get a working proxy or a reference
    if device is not None and isinstance(device, CustomProxy):
        d = device
    else:
        d = CustomProxy(device_path)

    if not d.isError():
        d.report_device()
        try:
            state = d.state()
            if state == DevState.FAULT or state == DevState.ALARM:
                d.error("Device has a ({}) state. Aborting the operation.".format(state))
            else:
                d.write_attribute(attr, value)
        except DevFailed:
            d.error("DevFailed upon accessing the device ()".format(d.device_path))
    return [WRITE_ATTRIBUTE, None]

def write_attribute_asynch(device_path, attr, value):
    """
    Writes an attribute value
    :param device_path:
    :param attr:
    :param value:
    :return:
    """
    d = CustomProxy(device_path)

    if not d.isError():
        d.report_device()
        try:
            state = d.state()
            if state != d.FAULT:
                d.write_attribute_asynch(attr, value)
            else:
                d.error("Device has a ({}) state. Aborting the operation.".format(d.FAULT))
        except d.DevFailed:
            d.error("DevFailed upon accessing the device ()".format(d.device_path))

    return [WRITE_ATTRIBUTE_ASYNCH, None]

def command_inout(device_path, cmd, *args):
    """
    Executes a command on the device
    :param device_path:
    :param cmd:
    :param args:
    :return:
    """
    res = None
    d = CustomProxy(device_path)

    if not d.isError():
        d.report_device()
        try:
            state = d.state()
            if state != d.FAULT:
                res = d.command_inout(cmd, *args)
            else:
                d.error("Device has a ({}) state. Aborting the operation.".format(d.FAULT))
        except d.DevFailed:
            d.error("DevFailed upon accessing the device ()".format(d.device_path))

    return [COMMAND_INOUT, res]

def command_inout_asynch(device_path, cmd, *args):
    """
    Executes a command on the device in asynch mode
    :param device_path:
    :param cmd:
    :param args:
    :return:
    """
    res = None
    d = CustomProxy(device_path)

    if not d.isError():
        d.report_device()
        d.error("Error ({})".format(d.isError()))
        try:
            state = d.state()
            if state != d.FAULT:
                res = d.command_inout_asynch(cmd, *args)
            else:
                d.error("Device has a ({}) state. Aborting the operation.".format(d.FAULT))
        except d.DevFailed:
            d.error("DevFailed upon accessing the device ()".format(d.device_path))

    return [COMMAND_INOUT_ASYNCH, res]

def wait_for_state(device_path, test_state, timeout, sleep_step=200):
    """
    Waits until a certain state is set for a device or until timeout
    :param device_path:
    :param test_state:
    :param timeout: time in ms
    :param sleep_step: time in ms
    :return:
    """
    d = CustomProxy(device_path)
    res = None

    if not d.isError():
        # convert to s
        timeout = float(timeout) / 1000.
        sleep_step = float(sleep_step) / 1000.

        d.report_device()
        try:
            # test state
            res = d.state()
            if res != d.FAULT:

                # test for a timeout
                counter = 0
                while res != test_state:
                    time.sleep(sleep_step)
                    counter += 1

                    # timeout is None
                    if counter * sleep_step >= timeout:
                        res = None
                        break

                    res = d.state()

            else:
                d.error("Device has a ({}) state. Aborting the operation.".format(d.FAULT))
        except d.DevFailed:
            d.error("DevFailed upon accessing the device ()".format(d.device_path))

    return [WAIT_FOR_STATE, res]

def read_attribute_as_string(device_path, attr, form="{}", device=None):
    """
    Reads a string attribute, performes a test for its value change
    :param device_path:
    :param attr:
    :return:
    """
    res = None
    default_res = "-"
    t = Tester()

    if device is not None and isinstance(device, CustomProxy):
        d = device
    else:
        d = CustomProxy(device_path)

    if not d.isError():


        # get a value, convert to a string
        d.report_device()
        try:
            state = d.state()
            if state == DevState.FAULT or state == DevState.ALARM:
                t.error("Device has a ({}) state. Aborting the operation.".format(state))
                raise DevFailed
            else:
                res = d.read_attribute(attr).value
                res = form.format(res)
        except (DevFailed, AttributeError) as e:
            t.error("DevFailed upon accessing the device ()".format(d.device_path))
            return res

        t.debug("Type of attribute ({}) value is ({})".format(attr, type(res)))

        # test for None value
        if not t.test(res):
            res = default_res

    return [d, res]

# @TODO: Implement timeout for device connection