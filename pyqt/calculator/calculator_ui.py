# -*- coding: utf-8 -*- 

# Form implementation generated from reading ui file 'calculator.ui'
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

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName(_fromUtf8("Calculator"))
        Calculator.resize(273, 159)
        self.labelFirstVal = QtGui.QLabel(Calculator)
        self.labelFirstVal.setGeometry(QtCore.QRect(10, 40, 51, 16))
        self.labelFirstVal.setObjectName(_fromUtf8("labelFirstVal"))
        self.labelSecondVal = QtGui.QLabel(Calculator)
        self.labelSecondVal.setGeometry(QtCore.QRect(150, 40, 71, 16))
        self.labelSecondVal.setObjectName(_fromUtf8("labelSecondVal"))
        self.lineFirstVal = QtGui.QLineEdit(Calculator)
        self.lineFirstVal.setGeometry(QtCore.QRect(10, 60, 113, 20))
        self.lineFirstVal.setObjectName(_fromUtf8("lineFirstVal"))
        self.lineSecondVal = QtGui.QLineEdit(Calculator)
        self.lineSecondVal.setGeometry(QtCore.QRect(150, 60, 113, 20))
        self.lineSecondVal.setObjectName(_fromUtf8("lineSecondVal"))
        self.labelResult = QtGui.QLabel(Calculator)
        self.labelResult.setGeometry(QtCore.QRect(10, 10, 241, 16))
        self.labelResult.setText(_fromUtf8(""))
        self.labelResult.setObjectName(_fromUtf8("labelResult"))
        self.comboOperator = QtGui.QComboBox(Calculator)
        self.comboOperator.setGeometry(QtCore.QRect(10, 110, 111, 22))
        self.comboOperator.setObjectName(_fromUtf8("comboOperator"))
        self.comboOperator.addItem(_fromUtf8(""))
        self.comboOperator.setItemText(0, _fromUtf8(""))
        self.comboOperator.addItem(_fromUtf8(""))
        self.comboOperator.addItem(_fromUtf8(""))
        self.comboOperator.addItem(_fromUtf8(""))
        self.comboOperator.addItem(_fromUtf8(""))
        self.labelOperator = QtGui.QLabel(Calculator)
        self.labelOperator.setGeometry(QtCore.QRect(10, 90, 51, 16))
        self.labelOperator.setObjectName(_fromUtf8("labelOperator"))
        self.ButtonCalculate = QtGui.QPushButton(Calculator)
        self.ButtonCalculate.setGeometry(QtCore.QRect(150, 102, 111, 31))
        self.ButtonCalculate.setObjectName(_fromUtf8("ButtonCalculate"))

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(_translate("Calculator", "Calculator", None))
        self.labelFirstVal.setText(_translate("Calculator", "First Value", None))
        self.labelSecondVal.setText(_translate("Calculator", "Second Value", None))
        self.comboOperator.setItemText(1, _translate("Calculator", "+", None))
        self.comboOperator.setItemText(2, _translate("Calculator", "-", None))
        self.comboOperator.setItemText(3, _translate("Calculator", "/", None))
        self.comboOperator.setItemText(4, _translate("Calculator", "*", None))
        self.labelOperator.setText(_translate("Calculator", "Operator", None))
        self.ButtonCalculate.setText(_translate("Calculator", "Calculate", None))

