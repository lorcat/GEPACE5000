# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(760, 482)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("QWidget {background-color: #fff;}\n"
"QLineEdit {height: 30px; border: 0px; font-size: 12px Arial; font-weight:bold; border-bottom: 1px solid #777; padding-top: 3px; padding-bottom: 3px; cursor: hand;}\n"
"QPushButton {border: 0px; font-weight:bold; background-color: #fafafa; padding: 5 10 5 10; border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: #ccc;}\n"
"QPushButton:hover {background-color: #eee; color: #777;}\n"
"QPushButton:pressed {background-color: #efe; color: #777;}\n"
"\n"
"QPushButton#btn_control_stop {background-color: #a33; color: #fff;}\n"
"QPushButton#btn_control_stop:hover {background-color: #c66; }\n"
"QPushButton#btn_control_stop:hover:pressed {background-color: #efe; color: #777;}\n"
"\n"
"QPushButton#btn_control_start {background-color: #3a3; color: #fff;}\n"
"QPushButton#btn_control_start:hover {background-color: #6c6; }\n"
"QPushButton#btn_control_start:hover:pressed {background-color: #efe; color: #777;}\n"
"\n"
"QPushButton#btn_decompress {background-color: #33a; color: #fff;}\n"
"QPushButton#btn_decompress:hover {background-color: #66a; }\n"
"QPushButton#btn_decompress:hover:pressed {background-color: #efe; color: #777;}\n"
"\n"
"QLineEdit#le_sp {background-color: #eee; font-size: 14px; height: 35px;}\n"
"QLineEdit#le_desiredsp {background-color: #fafafa; }\n"
"\n"
"QLineEdit#le_control_state {background-color: #fee; font-size: 14px; height: 35px;}\n"
"\n"
"QMenu {background-color: #fff;}\n"
"\n"
"QTabWidget { /* The tab widget frame */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 3px solid #acc;\n"
"    border-bottom: 3px solid #acc;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 0px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    padding-top: 5px; \n"
"    padding-bottom: 5px; \n"
"    padding-left: 15px; \n"
"    padding-right: 15px; \n"
"    width: 100px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    margin-left: 2px; \n"
"    margin-right: 2px;\n"
"    background-color: #acc;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"    background-color: #cdd;\n"
"    margin-top: 3px;\n"
"    font-color: #777;\n"
"}\n"
"\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 5px; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"\n"
"QTabBar::tab:first {\n"
"    margin-left: 5px; /* the first selected tab has nothing to overlap with on the left */\n"
"}"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 5, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabwdgt = QtGui.QTabWidget(self.centralwidget)
        self.tabwdgt.setObjectName(_fromUtf8("tabwdgt"))
        self.tab_compress = QtGui.QWidget()
        self.tab_compress.setObjectName(_fromUtf8("tab_compress"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_compress)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.tabwdgt.addTab(self.tab_compress, _fromUtf8(""))
        self.tab_decompress = QtGui.QWidget()
        self.tab_decompress.setObjectName(_fromUtf8("tab_decompress"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_decompress)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tabwdgt.addTab(self.tab_decompress, _fromUtf8(""))
        self.tab_advanced = QtGui.QWidget()
        self.tab_advanced.setObjectName(_fromUtf8("tab_advanced"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_advanced)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabwdgt.addTab(self.tab_advanced, _fromUtf8(""))
        self.tabwv = QtGui.QWidget()
        self.tabwv.setObjectName(_fromUtf8("tabwv"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabwv)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.wv_indicator = QtWebKit.QWebView(self.tabwv)
        self.wv_indicator.setMinimumSize(QtCore.QSize(0, 0))
        self.wv_indicator.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.wv_indicator.setObjectName(_fromUtf8("wv_indicator"))
        self.gridLayout_2.addWidget(self.wv_indicator, 0, 0, 1, 1)
        self.tabwdgt.addTab(self.tabwv, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabwdgt, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabwdgt.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabwdgt.setTabText(self.tabwdgt.indexOf(self.tab_compress), _translate("MainWindow", "Compress", None))
        self.tabwdgt.setTabToolTip(self.tabwdgt.indexOf(self.tab_compress), _translate("MainWindow", "Control elements for simple compression", None))
        self.tabwdgt.setTabText(self.tabwdgt.indexOf(self.tab_decompress), _translate("MainWindow", "Decompress", None))
        self.tabwdgt.setTabToolTip(self.tabwdgt.indexOf(self.tab_decompress), _translate("MainWindow", "Control elements for decompression", None))
        self.tabwdgt.setTabText(self.tabwdgt.indexOf(self.tab_advanced), _translate("MainWindow", "Advanced", None))
        self.tabwdgt.setTabToolTip(self.tabwdgt.indexOf(self.tab_advanced), _translate("MainWindow", "Advanced controls for the pressure device", None))
        self.tabwdgt.setTabText(self.tabwdgt.indexOf(self.tabwv), _translate("MainWindow", "Stats", None))
        self.tabwdgt.setTabToolTip(self.tabwdgt.indexOf(self.tabwv), _translate("MainWindow", "Current values of the polled attributes", None))

from PyQt4 import QtWebKit
