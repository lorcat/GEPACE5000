# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_view_advanced.ui'
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
        self.le_overshoot = QtGui.QLineEdit(Form)
        self.le_overshoot.setMinimumSize(QtCore.QSize(75, 20))
        self.le_overshoot.setAlignment(QtCore.Qt.AlignCenter)
        self.le_overshoot.setObjectName(_fromUtf8("le_overshoot"))
        self.gridLayout.addWidget(self.le_overshoot, 1, 0, 1, 2)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 2)
        self.le_slrtmode = QtGui.QLineEdit(Form)
        self.le_slrtmode.setMinimumSize(QtCore.QSize(75, 20))
        self.le_slrtmode.setAlignment(QtCore.Qt.AlignCenter)
        self.le_slrtmode.setObjectName(_fromUtf8("le_slrtmode"))
        self.gridLayout.addWidget(self.le_slrtmode, 1, 2, 1, 2)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(4)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btn_slrtmode_max = QtGui.QPushButton(self.widget)
        self.btn_slrtmode_max.setMinimumSize(QtCore.QSize(0, 24))
        self.btn_slrtmode_max.setObjectName(_fromUtf8("btn_slrtmode_max"))
        self.horizontalLayout_2.addWidget(self.btn_slrtmode_max)
        self.btn_slrtmode_linear = QtGui.QPushButton(self.widget)
        self.btn_slrtmode_linear.setMinimumSize(QtCore.QSize(0, 24))
        self.btn_slrtmode_linear.setObjectName(_fromUtf8("btn_slrtmode_linear"))
        self.horizontalLayout_2.addWidget(self.btn_slrtmode_linear)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addWidget(self.widget, 2, 2, 1, 2)
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_overshoot_on = QtGui.QPushButton(self.widget_2)
        self.btn_overshoot_on.setIconSize(QtCore.QSize(24, 24))
        self.btn_overshoot_on.setObjectName(_fromUtf8("btn_overshoot_on"))
        self.horizontalLayout.addWidget(self.btn_overshoot_on)
        self.btn_overshoot_off = QtGui.QPushButton(self.widget_2)
        self.btn_overshoot_off.setIconSize(QtCore.QSize(24, 24))
        self.btn_overshoot_off.setObjectName(_fromUtf8("btn_overshoot_off"))
        self.horizontalLayout.addWidget(self.btn_overshoot_off)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.widget_2, 2, 0, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 5)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btn_overshoot_on, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.actionOvershootOn)
        QtCore.QObject.connect(self.btn_overshoot_off, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.actionOvershootOff)
        QtCore.QObject.connect(self.btn_slrtmode_max, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.actionSlewrateMax)
        QtCore.QObject.connect(self.btn_slrtmode_linear, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.actionSlewrateLinear)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.le_overshoot, self.le_slrtmode)
        Form.setTabOrder(self.le_slrtmode, self.btn_overshoot_on)
        Form.setTabOrder(self.btn_overshoot_on, self.btn_overshoot_off)
        Form.setTabOrder(self.btn_overshoot_off, self.btn_slrtmode_max)
        Form.setTabOrder(self.btn_slrtmode_max, self.btn_slrtmode_linear)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.le_overshoot.setToolTip(_translate("Form", "Current value of Overshoot parameter", None))
        self.label_5.setText(_translate("Form", "Slewrate Mode", None))
        self.le_slrtmode.setToolTip(_translate("Form", "Current value of SlewRateMode parameter", None))
        self.label.setText(_translate("Form", "Overshoot", None))
        self.btn_slrtmode_max.setToolTip(_translate("Form", "Sets the SlewrateMode to MAX value (controller operates with maximum slew rate, SlewRate parameter is ignored)", None))
        self.btn_slrtmode_max.setText(_translate("Form", "Max", None))
        self.btn_slrtmode_linear.setToolTip(_translate("Form", "Sets the SlewrateMode to LINEAR value (controller operates a constant SlewRate)", None))
        self.btn_slrtmode_linear.setText(_translate("Form", "Linear", None))
        self.btn_overshoot_on.setToolTip(_translate("Form", "Sets the Overshoot parameter to ON state", None))
        self.btn_overshoot_on.setText(_translate("Form", "On", None))
        self.btn_overshoot_off.setToolTip(_translate("Form", "Sets the Overshoot parameter to OFF state", None))
        self.btn_overshoot_off.setText(_translate("Form", "Off", None))

import app_rc
