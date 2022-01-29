from PyQt5 import QtCore, QtGui, QtWidgets
import arithmetics

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setWindowModality(QtCore.Qt.NonModal)
		MainWindow.setEnabled(True)
		MainWindow.resize(360, 625)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
		MainWindow.setSizePolicy(sizePolicy)
		MainWindow.setMinimumSize(QtCore.QSize(360, 625))
		MainWindow.setMaximumSize(QtCore.QSize(360, 625))
		MainWindow.setBaseSize(QtCore.QSize(360, 625))
		icon = QtGui.QIcon("icon.ico")
		MainWindow.setWindowIcon(icon)
		MainWindow.setAnimated(True)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.calDisplay = QtWidgets.QLabel(self.centralwidget)
		self.calDisplay.setGeometry(QtCore.QRect(9, 19, 338, 128))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(22)
		self.calDisplay.setFont(font)
		self.calDisplay.setText("")
		self.calDisplay.setObjectName("calDisplay")
		self.calDisplay.setWordWrap(True)
		self.calDisplay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
		self.calFrame = QtWidgets.QFrame(self.centralwidget)
		self.calFrame.setGeometry(QtCore.QRect(9, 19, 340, 140))
		self.calFrame.setFrameShape(QtWidgets.QFrame.Box)
		self.calFrame.setFrameShadow(QtWidgets.QFrame.Plain)
		self.calFrame.setLineWidth(3)
		self.calFrame.setMidLineWidth(0)
		self.calFrame.setObjectName("calFrame")
		self.btnCubeRoot = QtWidgets.QPushButton(self.centralwidget)
		self.btnCubeRoot.setGeometry(QtCore.QRect(271, 271, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btnCubeRoot.sizePolicy().hasHeightForWidth())
		self.btnCubeRoot.setSizePolicy(sizePolicy)
		self.btnCubeRoot.setMinimumSize(QtCore.QSize(70, 50))
		self.btnCubeRoot.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btnCubeRoot.setFont(font)
		self.btnCubeRoot.setObjectName("btnCubeRoot")
		self.btn4 = QtWidgets.QPushButton(self.centralwidget)
		self.btn4.setGeometry(QtCore.QRect(19, 407, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
		self.btn4.setSizePolicy(sizePolicy)
		self.btn4.setMinimumSize(QtCore.QSize(70, 50))
		self.btn4.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btn4.setFont(font)
		self.btn4.setObjectName("btn4")
		self.btn1 = QtWidgets.QPushButton(self.centralwidget)
		self.btn1.setGeometry(QtCore.QRect(19, 475, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
		self.btn1.setSizePolicy(sizePolicy)
		self.btn1.setMinimumSize(QtCore.QSize(70, 50))
		self.btn1.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btn1.setFont(font)
		self.btn1.setObjectName("btn1")
		self.btnEquals = QtWidgets.QPushButton(self.centralwidget)
		self.btnEquals.setGeometry(QtCore.QRect(271, 543, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btnEquals.sizePolicy().hasHeightForWidth())
		self.btnEquals.setSizePolicy(sizePolicy)
		self.btnEquals.setMinimumSize(QtCore.QSize(70, 50))
		self.btnEquals.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btnEquals.setFont(font)
		self.btnEquals.setObjectName("btnEquals")
		self.btnDel = QtWidgets.QPushButton(self.centralwidget)
		self.btnDel.setGeometry(QtCore.QRect(187, 203, 153, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btnDel.sizePolicy().hasHeightForWidth())
		self.btnDel.setSizePolicy(sizePolicy)
		self.btnDel.setMinimumSize(QtCore.QSize(70, 50))
		self.btnDel.setMaximumSize(QtCore.QSize(200, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btnDel.setFont(font)
		self.btnDel.setObjectName("btnDel")
		self.btnSquareRoot = QtWidgets.QPushButton(self.centralwidget)
		self.btnSquareRoot.setGeometry(QtCore.QRect(187, 271, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btnSquareRoot.sizePolicy().hasHeightForWidth())
		self.btnSquareRoot.setSizePolicy(sizePolicy)
		self.btnSquareRoot.setMinimumSize(QtCore.QSize(70, 50))
		self.btnSquareRoot.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btnSquareRoot.setFont(font)
		self.btnSquareRoot.setObjectName("btnSquareRoot")
		self.btnSquare = QtWidgets.QPushButton(self.centralwidget)
		self.btnSquare.setGeometry(QtCore.QRect(19, 271, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btnSquare.sizePolicy().hasHeightForWidth())
		self.btnSquare.setSizePolicy(sizePolicy)
		self.btnSquare.setMinimumSize(QtCore.QSize(70, 50))
		self.btnSquare.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btnSquare.setFont(font)
		self.btnSquare.setObjectName("btnSquare")
		self.btn7 = QtWidgets.QPushButton(self.centralwidget)
		self.btn7.setGeometry(QtCore.QRect(19, 339, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
		self.btn7.setSizePolicy(sizePolicy)
		self.btn7.setMinimumSize(QtCore.QSize(70, 50))
		self.btn7.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btn7.setFont(font)
		self.btn7.setObjectName("btn7")
		self.btnDivide = QtWidgets.QPushButton(self.centralwidget)
		self.btnDivide.setGeometry(QtCore.QRect(187, 543, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btnDivide.sizePolicy().hasHeightForWidth())
		self.btnDivide.setSizePolicy(sizePolicy)
		self.btnDivide.setMinimumSize(QtCore.QSize(70, 50))
		self.btnDivide.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btnDivide.setFont(font)
		self.btnDivide.setObjectName("btnDivide")
		self.btn5 = QtWidgets.QPushButton(self.centralwidget)
		self.btn5.setGeometry(QtCore.QRect(103, 407, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
		self.btn5.setSizePolicy(sizePolicy)
		self.btn5.setMinimumSize(QtCore.QSize(70, 50))
		self.btn5.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btn5.setFont(font)
		self.btn5.setObjectName("btn5")
		self.btn9 = QtWidgets.QPushButton(self.centralwidget)
		self.btn9.setGeometry(QtCore.QRect(187, 339, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
		self.btn9.setSizePolicy(sizePolicy)
		self.btn9.setMinimumSize(QtCore.QSize(70, 50))
		self.btn9.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btn9.setFont(font)
		self.btn9.setObjectName("btn9")
		self.btn2 = QtWidgets.QPushButton(self.centralwidget)
		self.btn2.setGeometry(QtCore.QRect(103, 475, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
		self.btn2.setSizePolicy(sizePolicy)
		self.btn2.setMinimumSize(QtCore.QSize(70, 50))
		self.btn2.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btn2.setFont(font)
		self.btn2.setObjectName("btn2")
		self.btnClear = QtWidgets.QPushButton(self.centralwidget)
		self.btnClear.setGeometry(QtCore.QRect(19, 203, 153, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btnClear.sizePolicy().hasHeightForWidth())
		self.btnClear.setSizePolicy(sizePolicy)
		self.btnClear.setMinimumSize(QtCore.QSize(153, 50))
		self.btnClear.setMaximumSize(QtCore.QSize(153, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btnClear.setFont(font)
		self.btnClear.setObjectName("btnClear")
		self.btnDot = QtWidgets.QPushButton(self.centralwidget)
		self.btnDot.setGeometry(QtCore.QRect(103, 543, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btnDot.sizePolicy().hasHeightForWidth())
		self.btnDot.setSizePolicy(sizePolicy)
		self.btnDot.setMinimumSize(QtCore.QSize(70, 50))
		self.btnDot.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btnDot.setFont(font)
		self.btnDot.setObjectName("btnDot")
		self.btn6 = QtWidgets.QPushButton(self.centralwidget)
		self.btn6.setGeometry(QtCore.QRect(187, 407, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
		self.btn6.setSizePolicy(sizePolicy)
		self.btn6.setMinimumSize(QtCore.QSize(70, 50))
		self.btn6.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btn6.setFont(font)
		self.btn6.setObjectName("btn6")
		self.btn8 = QtWidgets.QPushButton(self.centralwidget)
		self.btn8.setGeometry(QtCore.QRect(103, 339, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
		self.btn8.setSizePolicy(sizePolicy)
		self.btn8.setMinimumSize(QtCore.QSize(70, 50))
		self.btn8.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btn8.setFont(font)
		self.btn8.setObjectName("btn8")
		self.btn3 = QtWidgets.QPushButton(self.centralwidget)
		self.btn3.setGeometry(QtCore.QRect(187, 475, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
		self.btn3.setSizePolicy(sizePolicy)
		self.btn3.setMinimumSize(QtCore.QSize(70, 50))
		self.btn3.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btn3.setFont(font)
		self.btn3.setObjectName("btn3")
		self.btn0 = QtWidgets.QPushButton(self.centralwidget)
		self.btn0.setGeometry(QtCore.QRect(19, 543, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btn0.sizePolicy().hasHeightForWidth())
		self.btn0.setSizePolicy(sizePolicy)
		self.btn0.setMinimumSize(QtCore.QSize(70, 50))
		self.btn0.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btn0.setFont(font)
		self.btn0.setObjectName("btn0")
		self.btnMultiply = QtWidgets.QPushButton(self.centralwidget)
		self.btnMultiply.setGeometry(QtCore.QRect(271, 339, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btnMultiply.sizePolicy().hasHeightForWidth())
		self.btnMultiply.setSizePolicy(sizePolicy)
		self.btnMultiply.setMinimumSize(QtCore.QSize(70, 50))
		self.btnMultiply.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btnMultiply.setFont(font)
		self.btnMultiply.setObjectName("btnMultiply")
		self.btnMinus = QtWidgets.QPushButton(self.centralwidget)
		self.btnMinus.setGeometry(QtCore.QRect(271, 407, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btnMinus.sizePolicy().hasHeightForWidth())
		self.btnMinus.setSizePolicy(sizePolicy)
		self.btnMinus.setMinimumSize(QtCore.QSize(70, 50))
		self.btnMinus.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btnMinus.setFont(font)
		self.btnMinus.setObjectName("btnMinus")
		self.btnCube = QtWidgets.QPushButton(self.centralwidget)
		self.btnCube.setGeometry(QtCore.QRect(103, 271, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btnCube.sizePolicy().hasHeightForWidth())
		self.btnCube.setSizePolicy(sizePolicy)
		self.btnCube.setMinimumSize(QtCore.QSize(70, 50))
		self.btnCube.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btnCube.setFont(font)
		self.btnCube.setObjectName("btnCube")
		self.btnPlus = QtWidgets.QPushButton(self.centralwidget)
		self.btnPlus.setGeometry(QtCore.QRect(271, 475, 70, 50))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btnPlus.sizePolicy().hasHeightForWidth())
		self.btnPlus.setSizePolicy(sizePolicy)
		self.btnPlus.setMinimumSize(QtCore.QSize(70, 50))
		self.btnPlus.setMaximumSize(QtCore.QSize(70, 50))
		font = QtGui.QFont()
		font.setFamily("Arial Black")
		font.setPointSize(25)
		self.btnPlus.setFont(font)
		self.btnPlus.setObjectName("btnPlus")
		MainWindow.setCentralWidget(self.centralwidget)

		self.btn1.clicked.connect(self.btn1Action)
		self.btn2.clicked.connect(self.btn2Action)
		self.btn3.clicked.connect(self.btn3Action)
		self.btn4.clicked.connect(self.btn4Action)
		self.btn5.clicked.connect(self.btn5Action)
		self.btn6.clicked.connect(self.btn6Action)
		self.btn7.clicked.connect(self.btn7Action)
		self.btn8.clicked.connect(self.btn8Action)
		self.btn9.clicked.connect(self.btn9Action)
		self.btn0.clicked.connect(self.btn0Action)
		self.btnDot.clicked.connect(self.btnDotAction)
		self.btnPlus.clicked.connect(self.btnPlusAction)
		self.btnMinus.clicked.connect(self.btnMinusAction)
		self.btnMultiply.clicked.connect(self.btnMultiplyAction)
		self.btnDivide.clicked.connect(self.btnDivideAction)
		self.btnSquareRoot.clicked.connect(self.btnSquareRootAction)
		self.btnSquare.clicked.connect(self.btnSquareAction)
		self.btnCubeRoot.clicked.connect(self.btnCubeRootAction)
		self.btnCube.clicked.connect(self.btnCubeAction)
		self.btnClear.clicked.connect(self.btnClearAction)
		self.btnEquals.clicked.connect(self.btnEqualsAction)
		self.btnDel.clicked.connect(self.btnDelAction)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
		self.btnCubeRoot.setText(_translate("MainWindow", "∛"))
		self.btn4.setText(_translate("MainWindow", "4"))
		self.btn1.setText(_translate("MainWindow", "1"))
		self.btnEquals.setText(_translate("MainWindow", "="))
		self.btnDel.setText(_translate("MainWindow", "<"))
		self.btnSquareRoot.setText(_translate("MainWindow", "√"))
		self.btnSquare.setText(_translate("MainWindow", "x2"))
		self.btn7.setText(_translate("MainWindow", "7"))
		self.btnDivide.setText(_translate("MainWindow", "/"))
		self.btn5.setText(_translate("MainWindow", "5"))
		self.btn9.setText(_translate("MainWindow", "9"))
		self.btn2.setText(_translate("MainWindow", "2"))
		self.btnClear.setText(_translate("MainWindow", "CE"))
		self.btnDot.setText(_translate("MainWindow", "."))
		self.btn6.setText(_translate("MainWindow", "6"))
		self.btn8.setText(_translate("MainWindow", "8"))
		self.btn3.setText(_translate("MainWindow", "3"))
		self.btn0.setText(_translate("MainWindow", "0"))
		self.btnMultiply.setText(_translate("MainWindow", "*"))
		self.btnMinus.setText(_translate("MainWindow", "-"))
		self.btnCube.setText(_translate("MainWindow", "x3"))
		self.btnPlus.setText(_translate("MainWindow", "+"))

	operators = ('+', '-', '*', '/', '√', '∛')
	powers = ('²', '³')

	def btn1Action(self):
		self.calDisplay.setText(self.calDisplay.text() + "1")

	def btn2Action(self):
		self.calDisplay.setText(self.calDisplay.text() + "2")

	def btn3Action(self):
		self.calDisplay.setText(self.calDisplay.text() + "3")

	def btn4Action(self):
		self.calDisplay.setText(self.calDisplay.text() + "4")

	def btn5Action(self):
		self.calDisplay.setText(self.calDisplay.text() + "5")

	def btn6Action(self):
		self.calDisplay.setText(self.calDisplay.text() + "6")

	def btn7Action(self):
		self.calDisplay.setText(self.calDisplay.text() + "7")

	def btn8Action(self):
		self.calDisplay.setText(self.calDisplay.text() + "8")

	def btn9Action(self):
		self.calDisplay.setText(self.calDisplay.text() + "9")

	def btn0Action(self):
		self.calDisplay.setText(self.calDisplay.text() + "0")

	def btnDotAction(self):
		display = self.calDisplay.text()
		try:
			if display[-1] == "." or display[-1] in (self.operators):
				pass
			else:
				self.calDisplay.setText(display + ".")
		except IndexError:
			pass

	def btnPlusAction(self):
		display = self.calDisplay.text()
		try:
			if display[-1] == "." or display[-1] in (self.operators):
				pass
			else:
				self.calDisplay.setText(display + "+")
		except IndexError:
			pass

	def btnMinusAction(self):
		display = self.calDisplay.text()
		try:
			if display[-1] == "." or (display[-1] == "-" and display[-2] == "-"):
				pass
			else:
				self.calDisplay.setText(display + "-")
		except IndexError:
			self.calDisplay.setText(display + "-")

	def btnMultiplyAction(self):
		display = self.calDisplay.text()
		try:
			if display[-1] == "." or display[-1] in (self.operators):
				pass
			else:
				self.calDisplay.setText(display + "*")
		except IndexError:
			pass

	def btnDivideAction(self):
		display = self.calDisplay.text()
		try:
			if display[-1] == "." or display[-1] in (self.operators):
				pass
			else:
				self.calDisplay.setText(display + "/")
		except IndexError:
			pass

	def btnSquareRootAction(self):
		display = self.calDisplay.text()
		try:
			if display[-1] == "." or display[-1] in (self.operators):
				pass
			else:
				self.calDisplay.setText(display + "√")
		except IndexError:
			self.calDisplay.setText(display + "√")

	def btnSquareAction(self):
		display = self.calDisplay.text()
		try:
			if display[-1] == "." or display[-1] in (self.operators) or display[-1] in (self.powers):
				pass
			else:
				self.calDisplay.setText(display + "²")
		except IndexError:
			pass

	def btnCubeRootAction(self):
		display = self.calDisplay.text()
		try:
			if display[-1] == "." or display[-1] in (self.operators):
				pass
			else:
				self.calDisplay.setText(display + "∛")
		except IndexError:
			self.calDisplay.setText(display + "∛")

	def btnCubeAction(self):
		display = self.calDisplay.text()
		try:
			if display[-1] == "." or display[-1] in (self.operators) or display[-1] in (self.powers):
				pass
			else:
				self.calDisplay.setText(display + "³")
		except IndexError:
			pass

	def btnClearAction(self):
		self.calDisplay.setText("")

	def btnEqualsAction(self):
		self.calDisplay.setText(arithmetics.Evaluate.evaluate(self.calDisplay.text()))

	def btnDelAction(self):
		self.calDisplay.setText(self.calDisplay.text()[:-1])
