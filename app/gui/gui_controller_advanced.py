from app.gui.gui_controller_abstract import *

from ui.ui_view_advanced import *

class AdvancedViewController(qtgui.QWidget, AbstractController, Ui_Form):
    def __init__(self, main_wnd, parent=None):
        qtgui.QWidget.__init__(self, parent=parent)
        AbstractController.__init__(self, main_wnd)

        # init interface
        self.setupUi(self)

        # widgets
        self.widget_list = {
            OVERSHOOT: {WDGT: self.le_overshoot, DATASTR: "", DATA: 0.},
            SLEWRATEMODE: {WDGT: self.le_slrtmode, DATASTR: "", DATA: 0.},
        }

    def actionSlewrateMax(self):
        """
        Setting the maximum slewrate mode
        :return:
        """
        self.debug("Setting the maximum slewrate mode")
        self.writeAttribute(SLEWRATEMODE, self.SLEWRATEMODE_MAX)


    def actionSlewrateLinear(self):
        """
        Setting the linear slewrate mode
        :return:
        """
        self.debug("Setting the linear slewrate mode")
        self.writeAttribute(SLEWRATEMODE, self.SLEWRATEMODE_LIN)

    def actionOvershootOn(self):
        """
        Setting the overshoot mode on
        :return:
        """
        self.debug("Setting the overshoot mode on")
        self.writeAttribute(OVERSHOOT, self.OVERSHOOT_ON)

    def actionOvershootOff(self):
        """
        Setting the overshoot mode off
        :return:
        """
        self.debug("Setting the overshoot mode off")
        self.writeAttribute(OVERSHOOT, self.OVERSHOOT_OFF)