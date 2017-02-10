from app.gui.gui_controller_abstract import *

from ui.ui_view_compress import *


class CompressViewController(qtgui.QWidget, AbstractController, Ui_Form):
    def __init__(self, main_wnd, parent=None):
        qtgui.QWidget.__init__(self, parent=parent)
        AbstractController.__init__(self, main_wnd)

        # init interface
        self.setupUi(self)

        # widgets
        self.widget_list = {
            SETPOINT: {WDGT: self.le_sp, DATASTR: "", DATA: 0.},
            SLEWRATE: {WDGT: self.le_slrt, DATASTR: "", DATA: self.SLEWRATE_MIN},
            PRESSURECONTROL: {WDGT: self.le_control_state, DATASTR: "", DATA: 0.},
        }

        # preparing validators
        self.addWdgtDblValidator(self.le_desiredsp, self.SETPOINT_MIN, self.SETPOINT_MAX, self.SETPOINT_DELIM)
        self.addWdgtDblValidator(self.le_sp_step, self.SETPOINT_MIN, self.SETPOINT_MAX, self.SETPOINT_DELIM)
        self.addWdgtDblValidator(self.le_slrt_step, self.SLEWRATE_MIN, self.SLEWRATE_MAX, self.SLEWRATE_DELIM)

        # test default values
        self.setWdgtDefaultValue(self.le_slrt_step, self.SLEWRATE_STEP_DEFAULT)
        self.setWdgtDefaultValue(self.le_sp_step, self.SETPOINT_STEP_DEFAULT)

        # custom context menu
        self.le_slrt_step.contextMenuEvent = lambda w=self.le_slrt_step, b=self.le_slrt_step, a=SLEWRATE, d="": self.createCustomContextMenu(w, d, [a, b])
        self.le_sp_step.contextMenuEvent = lambda w=self.le_sp_step, b=self.le_sp_step, a=SETPOINT, d="": self.createCustomContextMenu(w, d, [a, b])
        self.le_desiredsp.contextMenuEvent = lambda w=self.le_desiredsp, b=self.le_desiredsp, a="", d="": self.createCustomContextMenu(w, d, [a, b])

    def actionStartControl(self):
        """
        Starts the pump control
        :return:
        """
        self.debug("Starting the pump control")

        self.writeAttribute(PRESSURECONTROL, self.PRESSURECONTROL_ON)

    def actionSlrtUp(self):
        """
        Increasing the slewrate value
        :return:
        """
        self.debug("Increasing the slew rate value")

        self.changeValueByStep(SLEWRATE, self.le_slrt_step, self.SLEWRATE_MIN, self.SLEWRATE_MAX, sign=1)

    def actionSlrtDw(self):
        """
        Decreasing the slewrate value
        :return:
        """
        self.debug("Decreasing the slew rate value")
        self.changeValueByStep(SLEWRATE, self.le_slrt_step, self.SLEWRATE_MIN, self.SLEWRATE_MAX, sign=-1)

    def actionSPUp(self):
        """
        Increasing the setpoint value
        :return:
        """
        self.debug("Increasing the set point value")

        sign = 1
        try:
            self.checkWdgtValidator(self.le_desiredsp)
            self.checkWdgtValidator(self.le_sp_step)

            # ok - sending the value to the device
            step = float(self.le_sp_step.text())
            value = float(self.le_desiredsp.text())

            # test for the range
            if value + sign * step < self.SETPOINT_MIN or value + sign * step > self.SETPOINT_MAX:
                return

            self.le_desiredsp.setText(str(value+sign*step))
        except ValueError:
            msg = "Wrong parameter for step value or desired value"
            qtgui.QMessageBox.critical(self.main_wnd, "Error", msg)
            self.error(msg)

    def actionSPDw(self):
        """
        Decreasing the setpoint value
        :return:
        """
        self.debug("Decreasing the set point value")

        sign = -1
        try:
            self.checkWdgtValidator(self.le_desiredsp)
            self.checkWdgtValidator(self.le_sp_step)

            # ok - sending the value to the device
            step = float(self.le_sp_step.text())
            value = float(self.le_desiredsp.text())

            # test for the range
            if value + sign * step < self.SETPOINT_MIN or value + sign * step > self.SETPOINT_MAX:
                return

            self.le_desiredsp.setText(str(value + sign*step))
        except ValueError:
            msg = "Wrong parameter for step value or desired value"
            qtgui.QMessageBox.critical(self.main_wnd, "Error", msg)
            self.error(msg)

    def actionApplySetPoint(self):
        """
        Applies the set point to the pump
        :return:
        """
        self.debug("Applies the set point to the pump")

        try:
            self.checkWdgtValidator(self.le_desiredsp)

            # ok - sending the value to the device
            value = float(self.le_desiredsp.text())
            self.writeAttribute(SETPOINT, value)
        except ValueError:
            msg = "Could not process current set point value"
            qtgui.QMessageBox.critical(self.main_wnd, "Error", msg)
            self.error(msg)

    def processAttributes(self, data):
        """
        Processes an attribute update event and applies new values to the status fields if needed
        :param data:
        :return:
        """
        AbstractController.processAttributes(self, data)

        for (i, el) in enumerate(data):
            key = None
            try:
                key = ATTR
                if el[key] == SETPOINT and len(str(self.le_desiredsp.text())) == 0:
                    self.le_desiredsp.setText(self.le_sp.text())
            except AttributeError:
                self.error("Error on processing new data, no key ({})".format(key))
