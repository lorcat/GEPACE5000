from app.gui.gui_controller_abstract import *

from ui.ui_view_decompress import *

class DecompressViewController(qtgui.QWidget, AbstractController, Ui_Form):
    def __init__(self, main_wnd, parent=None):
        qtgui.QWidget.__init__(self, parent=parent)
        AbstractController.__init__(self, main_wnd)

        # init interface
        self.setupUi(self)

        # widgets
        self.widget_list = {
            DECOMPRESSRATE: {WDGT: self.le_slrt, DATASTR: "", DATA: 0.},
            PRESSURECONTROL: {WDGT: self.le_control_state, DATASTR: "", DATA: 0.},
        }

        # preparing validators
        self.addWdgtDblValidator(self.le_slrt_step, self.SLEWRATE_MIN, self.SLEWRATE_MAX, self.SLEWRATE_DELIM)

        # test default values
        self.setWdgtDefaultValue(self.le_slrt_step, self.SLEWRATE_STEP_DEFAULT)

        # custom context menu
        self.le_slrt_step.contextMenuEvent = lambda w=self.le_slrt_step, b=self.le_slrt_step, a=DECOMPRESSRATE, d="": self.createCustomContextMenu(w, d, [a, b])

    def actionDecompress(self):
        """
        Starts the pump decompression
        :return:
        """
        self.debug("Starting the pump decompression")
        self.runCommand(self.CMD_DECOMPRESS)


    def actionSlrtUp(self):
        """
        Increasing the decompression slewrate value
        :return:
        """
        self.debug("Trying to increase the decompression slewrate value")
        self.changeValueByStep(DECOMPRESSRATE, self.le_slrt_step, self.SLEWRATE_MIN, self.SLEWRATE_MAX, sign=1)

    def actionSlrtDw(self):
        """
        Decreasing the decompression slewrate value
        :return:
        """
        self.debug("Trying to decreasing the decompression slewrate value")
        self.changeValueByStep(DECOMPRESSRATE, self.le_slrt_step, self.SLEWRATE_MIN, self.SLEWRATE_MAX, sign=-1)