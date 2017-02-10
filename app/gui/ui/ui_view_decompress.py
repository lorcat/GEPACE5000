# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_view_decompress.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(541, 289)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(4)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btn_decompress = QtGui.QPushButton(self.widget)
        self.btn_decompress.setMinimumSize(QtCore.QSize(0, 32))
        self.btn_decompress.setObjectName(_fromUtf8("btn_decompress"))
        self.verticalLayout.addWidget(self.btn_decompress)
        self.btn_control_stop = QtGui.QPushButton(self.widget)
        self.btn_control_stop.setMinimumSize(QtCore.QSize(0, 32))
        self.btn_control_stop.setObjectName(_fromUtf8("btn_control_stop"))
        self.verticalLayout.addWidget(self.btn_control_stop)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.widget, 2, 2, 4, 2)
        self.le_slrt_step = QtGui.QLineEdit(Form)
        self.le_slrt_step.setMinimumSize(QtCore.QSize(75, 20))
        self.le_slrt_step.setAlignment(QtCore.Qt.AlignCenter)
        self.le_slrt_step.setReadOnly(False)
        self.le_slrt_step.setObjectName(_fromUtf8("le_slrt_step"))
        self.gridLayout.addWidget(self.le_slrt_step, 3, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 4, 1, 1)
        self.le_slrt = QtGui.QLineEdit(Form)
        self.le_slrt.setMinimumSize(QtCore.QSize(75, 20))
        self.le_slrt.setAlignment(QtCore.Qt.AlignCenter)
        self.le_slrt.setObjectName(_fromUtf8("le_slrt"))
        self.gridLayout.addWidget(self.le_slrt, 1, 0, 1, 2)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 2)
        self.le_control_state = QtGui.QLineEdit(Form)
        self.le_control_state.setMinimumSize(QtCore.QSize(75, 20))
        self.le_control_state.setAlignment(QtCore.Qt.AlignCenter)
        self.le_control_state.setObjectName(_fromUtf8("le_control_state"))
        self.gridLayout.addWidget(self.le_control_state, 1, 2, 1, 2)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 6, 2, 1, 1)
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_slrtdw = QtGui.QPushButton(self.widget_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/a_dw.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_slrtdw.setIcon(icon)
        self.btn_slrtdw.setIconSize(QtCore.QSize(24, 24))
        self.btn_slrtdw.setObjectName(_fromUtf8("btn_slrtdw"))
        self.horizontalLayout.addWidget(self.btn_slrtdw)
        self.btn_slrtup = QtGui.QPushButton(self.widget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/a_up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_slrtup.setIcon(icon1)
        self.btn_slrtup.setIconSize(QtCore.QSize(24, 24))
        self.btn_slrtup.setObjectName(_fromUtf8("btn_slrtup"))
        self.horizontalLayout.addWidget(self.btn_slrtup)
        self.gridLayout.addWidget(self.widget_2, 4, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btn_decompress, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.actionDecompress)
        QtCore.QObject.connect(self.btn_control_stop, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.actionStopControl)
        QtCore.QObject.connect(self.btn_slrtup, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.actionSlrtUp)
        QtCore.QObject.connect(self.btn_slrtdw, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.actionSlrtDw)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.le_slrt, self.le_control_state)
        Form.setTabOrder(self.le_control_state, self.le_slrt_step)
        Form.setTabOrder(self.le_slrt_step, self.btn_decompress)
        Form.setTabOrder(self.btn_decompress, self.btn_control_stop)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btn_decompress.setToolTip(_translate("Form", "Starts decompression (decompression rate is copied to the slew rate)", None))
        self.btn_decompress.setText(_translate("Form", "Decompress", None))
        self.btn_control_stop.setToolTip(_translate("Form", "Stops operation of the pressure controller", None))
        self.btn_control_stop.setText(_translate("Form", "Stop", None))
        self.le_slrt_step.setToolTip(_translate("Form", "Decompression rate step", None))
        self.le_slrt.setToolTip(_translate("Form", "Current value of the decompression slewrate", None))
        self.label_5.setText(_translate("Form", "Press. Controller State", None))
        self.le_control_state.setToolTip(_translate("Form", "Pressure controller state", None))
        self.label_2.setText(_translate("Form", "Step", None))
        self.label.setText(_translate("Form", "Decompr. slewrate, bar/min", None))
        self.btn_slrtdw.setToolTip(_translate("Form", "Decrease decompression slew rate (applied immediately)", None))
        self.btn_slrtdw.setText(_translate("Form", "Down", None))
        self.btn_slrtup.setToolTip(_translate("Form", "Increase decompression slew rate (applied immediately)", None))
        self.btn_slrtup.setText(_translate("Form", "Up", None))

import app_rc
