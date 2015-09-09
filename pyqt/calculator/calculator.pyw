import sys
from calculator_ui import *

class Calculator(QtGui.QDialog):

	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Calculator()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.ButtonCalculate, QtCore.SIGNAL('clicked()'),self.calculateVal)
		
	def calculateVal(self):
		firstVal = self.getValue(self.ui.lineFirstVal)	
		secondVal = self.getValue(self.ui.lineSecondVal)
		#self.ui.comboOperator.currentIndex()	
		if( len(self.ui.comboOperator.currentText()) != 0):
			operator = self.ui.comboOperator.currentText()
			result = self.getResult(firstVal, secondVal, operator)	
		else:
			result = 'Invalid Operator'	
		self.ui.labelResult.setText(result)	
		
	def getValue(self, lineValue):
		if( len(lineValue.text()) != 0):
			return int(lineValue.text())
		else:
			return 0
	
	def getResult(self, firstVal, secondVal, operator):
		if(operator == '+'):
			return str( firstVal + secondVal )
		if(operator == '-'):
			return str( firstVal - secondVal )
		if(operator == '/'):
			return str( firstVal / secondVal )
		if(operator == '*'):
			return str( firstVal * secondVal )	
	
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	calc = Calculator()
	calc.show()
	sys.exit(app.exec_())