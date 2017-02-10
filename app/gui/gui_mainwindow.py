__author__ = 'Konstantin Glazyrin'

# main common libraries
from app.load import *

# specific libraries
from app.load.load_config import *
from app.load.load_runnables import *

# controllers
from app.load.load_controllers import *

# ui
from app.gui.ui.ui_mainwindow import Ui_MainWindow

class CustomMainWindow(qtgui.QMainWindow, Tester, Ui_MainWindow):
    # template to use with JS handling
    TEMPL_JSINDICATOR = "ExtQt.parseNewData(%DATA%)"
    TEMPL_JSINDICATOR_SUB = "%DATA%"

    # MENU names
    MENU_CONTROLLERS = "&Controllers"

    def __init__(self, starter, parent=None):
        qtgui.QMainWindow.__init__(self, parent=parent)
        Tester.__init__(self)

        # starter object
        self._starter = None
        if self.test(starter):
            self._starter = starter

        # pool to run single task workers
        self.thread_pool = getPool()

        self.__init_gui()
        self.__init_events()

    def __init_gui(self):
        """
        Initializes gui
        :return:
        """
        self.debug("Initializing gui")

        self.setupUi(self)

        # change functions fired for the buttons related to the controllers (reader+writer)
        if self.test(self._starter):
            pass

        # initializes html
        self.initializeHTML()

        # initializes tab widget
        self.initializeTabWdgt()

        # prepare menu
        self.initializeMenu()

        # make cosmetic changes - icon, title
        self._initIcon()
        self._initTitle()
        self.show()

        self.startReaderTimer()

    def initializeHTML(self):
        """
        Initializing HTML page for the profile
        :return:
        """
        fn_indicator = os.path.join(config.RESOURCES[RESOURCE_HTML], config.PROFILES[PROFILE_START][PROFILE_HTML])
        self.debug("Setting Indicators HTML page ({})".format(fn_indicator))

        # URL
        url_indicator = qtcore.QUrl()
        url_indicator.setPath(fn_indicator)

        # initilize JS events for software page
        _frame_software = self.wv_indicator.page().mainFrame()
        self.connect(_frame_software, qtcore.SIGNAL("javaScriptWindowObjectCleared()"), self.processReloadIndicatorPage)
        self.connect(self.wv_indicator, qtcore.SIGNAL("loadFinished (bool)"), self.processReloadIndicatorPage)
        self.wv_indicator.setUrl(url_indicator)

    def initializeMenu(self):
        """
        Initializes main program menu
        :return:
        """
        self.debug("Adding menu.")
        mb = self.menuBar()

        # adding menu with controllers - executables to run
        self.ctrl_menu = mb.addMenu(self.MENU_CONTROLLERS)
        for (i, el) in enumerate(config.PROFILES[PROFILE_START][PROFILE_CONTROLLERS]):
            try:
                key = CMD
                if el[key] != SEPARATOR:
                    key = NICK
                    self.debug("Adding action ({}:{})".format(key, el[key]))
                    act = QtGui.QAction(el[key], self.ctrl_menu)
                    self.ctrl_menu.addAction(act)
                else:
                    self.debug("Adding separator")
                    self.ctrl_menu.addSeparator()
            except KeyError:
                self.error("Configuration error; key ({}) does not exist, skipping controller..".format(key))
                continue

        # initialize events for controllers
        self.connect(self.ctrl_menu, QtCore.SIGNAL("triggered(QAction*)"), self.processControllersMenu)

    def initializeTabWdgt(self):
        """
        Initializes main window tab widget
        :return:
        """
        self.debug("Initializing tab widget")
        self.wdgt_compress = CompressViewController(self)
        self.wdgt_decompress = DecompressViewController(self)
        self.wdgt_advanced = AdvancedViewController(self)

        self.tab_compress.layout().addWidget(self.wdgt_compress)
        self.tab_decompress.layout().addWidget(self.wdgt_decompress)
        self.tab_advanced.layout().addWidget(self.wdgt_advanced)

    def __init_events(self):
        """
        Initializes events
        :return:
        """
        self.debug("Initializing events")

    def _initIcon(self):
        """
        Sets the icon for the window
        :return:
        """
        self.debug("Preparing window icon")

        path = config.RESOURCES[RESOURCE_IMAGES]
        self.debug("Preparing image path, directory ({})".format(path))

        res = None
        dir = qtcore.QDir(path)
        temp = qtcore.QFileInfo()
        temp.setFile(dir, 'program_icon.png')
        if temp.isFile():
            self.setWindowIcon(qtgui.QIcon(qtgui.QPixmap(temp.absoluteFilePath())))

        return res

    def _initTitle(self):
        """
        Changes title of the window depending on the profile name
        :return:
        """
        title = config.PROFILES[PROFILE_START][PROFILE_NAME]
        self.debug("Preparing window title ({})".format(title))
        self.setWindowTitle(title)

    def reportJSNewData(self, data):
        """
        Reports new data to the javascript object underneath the HTML page
        :param temp_data:
        :return:
        """
        ref_data = deepcopy(data)

        self.debug("Reporting new temp_data ({}) to the html page".format(ref_data))

        temp_data = str(ref_data)
        # handle unusual situations : None, etc
        temp_data = temp_data.replace("None", "null")

        jsmsg = self.TEMPL_JSINDICATOR.replace(self.TEMPL_JSINDICATOR_SUB, temp_data)

        self.debug("JS temp_data ({})".format(jsmsg))
        self.wv_indicator.page().mainFrame().evaluateJavaScript(jsmsg)

        if len(ref_data) > 0:
            del ref_data[:]

    @qtcore.pyqtSlot()
    def processReloadIndicatorPage(self, *args):
        """
        Processes events on html page reload for indicator page - adds an javascript object
        :return:
        """
        self.wv_indicator.page().mainFrame().addToJavaScriptWindowObject("qtWindow", self)


    def startReaderTimer(self):
        """
        Starts internal reading timer initializing the reader
        :return:
        """
        self.debug("Starting internal timer initializing the reader")
        self._reader_timer = qtcore.QTimer(self)
        self._reader_timer.setSingleShot(True)
        self._reader_timer.setInterval(500)

        self.connect(self._reader_timer, qtcore.SIGNAL("timeout()"), self.initReaderTimer)

        self._reader_timer.start()

    def initReaderTimer(self):
        """
        Finalizes initialization of the reader
        :return:
        """
        self.debug("Initializing the reader")
        if self._reader_timer.isActive():
            self._reader_timer.stop()
        self._reader_timer.deleteLater()

        # initialize event propagation for new data
        self._starter.ctrl_reader.registerNewData(self.wdgt_compress.processAttributes)
        self._starter.ctrl_reader.registerNewData(self.wdgt_decompress.processAttributes)
        self._starter.ctrl_reader.registerNewData(self.wdgt_advanced.processAttributes)

        self._starter.ctrl_reader.startReader()

    def processControllersMenu(self, action):
        """
        Processes actions with controller menu
        :param action:
        :return:
        """
        self.debug("Processing controller menu action ({})".format(action))
        for (i, act) in enumerate(self.ctrl_menu.actions()):
            if act == action:
                self.debug("Action is found")
                key = None
                try:
                    key = CMD
                    cmd_name = config.PROFILES[PROFILE_START][PROFILE_CONTROLLERS][i][key]
                    key = ARGS
                    cmd_args = config.PROFILES[PROFILE_START][PROFILE_CONTROLLERS][i][key]

                    runner = ProcessRunner(cmd_name, cmd_args)
                    self.thread_pool.tryStart(runner)
                except KeyError:
                    self.error("Configuration error; key ({}) does not exist..".format(key))

                break

# @TODO: check menu operation
# @TODO: adjust style
# @TODO: change icons + splash