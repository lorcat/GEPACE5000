__author__ = 'Konstantin Glazyrin'

from PyQt4 import QtGui, QtCore

from app.common import Tester
from app.gui.gui_splash import SplashWindow
from app.gui.gui_profiledialog import ProfileDialog

from app.config.keys import *
from app.config import configuration as config

from app.reader.controller import ReaderController
from app.writer.controller import WriterController
from app.grapher.controller import GraphController

from app.gui.gui_mainwindow import CustomMainWindow
from app.runnables import getPool

# main class showing the splash screen and starting main window
class Starter(QtCore.QObject, Tester):
    DELAY = 100

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent=parent)
        Tester.__init__(self)

        self.debug("Initializing - starting timer")
        self._timerid = self.startTimer(self.DELAY)

        # splash screen
        self._splash = None
        # main window handle
        self._mainwnd = None

        # controllers
        # reader - obtaining data
        self.ctrl_reader = None
        # writer - saving data
        self.ctrl_writer = None
        # graph controller
        self.ctrl_graph = None

        # thread pool to start one time workers
        self.thread_pool = getPool(parent=self)

    def timerEvent(self, event):
        """
        Event fired on timer - event loop engaged
        :param event:
        :return:
        """
        self.debug("Initializing - killing timer")
        self.killTimer(self._timerid)

        # selecting profile
        profile = ProfileDialog()
        res = profile.exec_()
        self.debug("Result of the profile selection ({})".format(res))
        if res == 0:
            return

        if not self.test(profile.module):
            self.exitWithError("No profile has been selected")
            return

        # populate profile information or exit
        try:
            config.PROFILES[PROFILE_START] = profile.module.START
        except AttributeError:
            self.exitWithError("The profile is malformed - no START dict()")
            return

        # test profile - that necessary fields are present
        for el in [PROFILE_ATTRLOOP, PROFILE_DELAY, PROFILE_HTML, PROFILE_TANGO_ADDRESS, PROFILE_NAME]:
            try:
                v = config.PROFILES[PROFILE_START][el]
            except KeyError:
                self.exitWithError("The selected profile is malformed - element ({}) is not present".format(el))
                return

        # showing splash, initializing events
        self._splash = SplashWindow()
        self._splash.registerFinished(self.showMainWindow)

        # go through the initialization parts
        self.initializeApp()

    def showMainWindow(self):
        """
        Starts the main application window
        :return:
        """
        self.debug("Initializing - starting main application window")

        # create the window and register the most important events
        self._mainwnd = CustomMainWindow(self)

        self.ctrl_reader.registerNewData(self._mainwnd.reportJSNewData)

    def initializeApp(self):
        """
        Initializes controllers, main operations
        :return:
        """
        self.debug("Initializing - application (controllers, events)")

        self._splash.setProgress("reader controller", 0, 100)
        # initialize reader controller
        self.ctrl_reader = ReaderController(parent=self)

        self._splash.setProgress("writer controller", 10, 100)
        self.ctrl_writer = WriterController(parent=self)

        self._splash.setProgress("graph controller", 20, 100)
        self.ctrl_graph = GraphController(parent=self)

        # connect reader and writer
        self.ctrl_reader.registerNewData(self.ctrl_writer.reportNewData)
        self.ctrl_reader.registerNewData(self.ctrl_graph.reportNewData)

        # events
        # cleaning up upon closing the last window
        self._splash.setProgress("qt events", 90, 100)
        self.connect(QtGui.QApplication.instance(), QtCore.SIGNAL("lastWindowClosed()"), self.cleanup)
        self._splash.setProgress("done", 100, 100)

    def exitWithError(self, msg):
        """
        Stops application execution and reports a message
        :param msg:
        :return:
        """
        self.debug("Exiting with an error message ({})".format(str(msg)))
        # show the error message
        self.error(msg)

        # cleanup the object
        self.cleanup()

        return

    def cleanup(self, brestart=False):
        """
        Cleans up the application
        :return:
        """
        self.debug("Exiting the application - cleaning up")

        # hide the window if necessary
        if self.test(self._mainwnd, CustomMainWindow):
            self._mainwnd.hide()

        # cleaning up reader
        if self.test(self.ctrl_reader, ReaderController):
            self.ctrl_reader.cleanup()

        # cleaning up writer
        if self.test(self.ctrl_writer, WriterController):
            self.ctrl_writer.cleanup()

        # cleaning up grapher
        if self.test(self.ctrl_graph, GraphController):
            self.ctrl_graph.cleanup()

        # cleaning up the thread pool
        if self.test(self.thread_pool):
            self.thread_pool.cleanup()

        # restart program if requested
        app = QtGui.QApplication.instance()
        if brestart:
            args = list(app.arguments())
            temp_app = args.pop(0)

            self.debug("Restarting the application ({}:{})".format(temp_app, args))
            QtCore.QProcess.startDetached(temp_app, args)

        # finish the application
        app.quit()


