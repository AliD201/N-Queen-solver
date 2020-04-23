# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\asus\Desktop\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import threading
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
	QGridLayout, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QColor, QImage
from PyQt5.QtCore import pyqtSlot, QSize
import Hill as Hill

import SimulatedAnnealing as SA
import local_beam as LB
import Genetic as GN


stop_it = False
sa_list = list()
choicePerc = float()
boardcounter = 0
hilllists = list()
hillcondition = False
localBoards = list()
localCondition = True
geneticcondition = False
All_lists_genetic = list()
Gboardcounter = 0
solGen = list()
energy_list = list()
speed = 0
prev = False

class Color(QWidget):

	def __init__(self, r, b, g, *args, **kwargs):
		super(Color, self).__init__(*args, **kwargs)
		self.setAutoFillBackground(True)
		#self.setStyleSheet("border:1px solid rgb(0, 255, 0);")
		#self.frame = QtWidgets.QFrame(self.centralwidget)
		palette = self.palette()
		palette.setColor(QPalette.Window, QColor(r, b, g, 255))
		self.setPalette(palette)

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(789, 576)
		MainWindow.setWindowTitle("Heuristic Algorithms")
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(56)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
		MainWindow.setSizePolicy(sizePolicy)
		MainWindow.setMinimumSize(QtCore.QSize(789, 576))
		MainWindow.setMaximumSize(QtCore.QSize(789, 576))
		MainWindow.setSizeIncrement(QtCore.QSize(789, 576))
		MainWindow.setBaseSize(QtCore.QSize(789, 576))
		font = QtGui.QFont()
		font.setBold(False)
		font.setWeight(50)
		MainWindow.setFont(font)
		MainWindow.setAccessibleName("")
		MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		MainWindow.setAnimated(True)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.frame = QtWidgets.QFrame(self.centralwidget)
		self.frame.setEnabled(True)
		self.frame.setGeometry(QtCore.QRect(10, 10, 541, 541))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(9)
		sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
		self.frame.setSizePolicy(sizePolicy)
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.frame.setLineWidth(5)
		self.frame.setObjectName("frame")

		self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
		self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 521, 531))
		self.groupBox_3.setObjectName("groupBox_3")
		self.groupBox_3.setTitle("N-Queens")
		
		#self.horizontalGroupBox = QGroupBox("Grid")
		self.layout = QGridLayout()
		self.groupBox_3.setLayout(self.layout)

		#layout.setColumnStretch(0, 1)
		#layout.setColumnStretch(1, 1)
		#layout.setColumnStretch(2, 1)
		

		


		
		self.frame_2 = QtWidgets.QFrame(self.centralwidget)
		self.frame_2.setGeometry(QtCore.QRect(560, 10, 221, 541))
		self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.frame_2.setObjectName("frame_2")
		self.groupBox = QtWidgets.QGroupBox(self.frame_2)
		self.groupBox.setEnabled(True)
		self.groupBox.setGeometry(QtCore.QRect(10, 50, 201, 151))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.groupBox.setFont(font)
		self.groupBox.setAutoFillBackground(False)
		self.groupBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
		self.groupBox.setFlat(False)
		self.groupBox.setCheckable(False)
		self.groupBox.setObjectName("groupBox")
		self.groupBox.setTitle("Algorithms")
		self.radioButton = QtWidgets.QRadioButton(self.groupBox)
		self.radioButton.setGeometry(QtCore.QRect(10, 30, 121, 17))
		self.radioButton.setObjectName("radioButton")
		self.radioButton.setText("Hill Climbing")
		self.radioButton.setEnabled(False)
		self.radioButton.toggled.connect(self.hillOptions)
		self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
		self.radioButton_2.setGeometry(QtCore.QRect(10, 60, 121, 17))
		self.radioButton_2.setObjectName("radioButton_4")
		self.radioButton_2.setText("Local Beam")
		self.radioButton_2.setEnabled(False)
		self.radioButton_2.toggled.connect(self.locOptions)

		self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
		self.radioButton_3.setGeometry(QtCore.QRect(10, 90, 151, 17))
		self.radioButton_3.setObjectName("radioButton_2")
		self.radioButton_3.setText("Simulated annieling")
		self.radioButton_3.setEnabled(False)
		self.radioButton_3.toggled.connect(self.saOptions)
		self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
		self.radioButton_4.setGeometry(QtCore.QRect(10, 120, 141, 17))
		self.radioButton_4.setObjectName("radioButton_3")
		self.radioButton_4.setText("Genetic algorithm")
		self.radioButton_4.setEnabled(False)
		self.radioButton_4.toggled.connect(self.geOptions)


		self.label = QtWidgets.QLabel(self.frame_2)
		self.label.setGeometry(QtCore.QRect(10, 20, 81, 20))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.label.setText("Board size (N):")
		self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
		self.groupBox_2.setGeometry(QtCore.QRect(10, 210, 201, 151))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.groupBox_2.setFont(font)
		self.groupBox_2.setAutoFillBackground(False)
		self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
		self.groupBox_2.setFlat(False)
		self.groupBox_2.setCheckable(False)
		self.groupBox_2.setObjectName("groupBox_2")
		self.groupBox_2.setTitle("Parameters")

		self.checkbox = QtWidgets.QCheckBox(self.groupBox_2)
		self.checkbox.setGeometry(QtCore.QRect(10, 20, 81, 16))
		self.checkbox.setObjectName("checkbox")
		self.checkbox.setText("Stochastic")
		self.checkbox.hide()

		# hill climbing radio
		self.hillabel = QtWidgets.QLabel(self.groupBox_2)
		self.hillabel.setGeometry(QtCore.QRect(10, 50, 61, 21))
		self.hillabel.setObjectName("hillabel")
		self.hillabel.setText("initialize")
		self.hillabel.hide()

		self.hillinitial = QtWidgets.QSpinBox(self.groupBox_2)
		self.hillinitial.setGeometry(QtCore.QRect(70, 50, 42, 22))
		self.hillinitial.setObjectName("hillinitial")
		self.hillinitial.setMinimum(1)
		self.hillinitial.setMaximum(15)
		self.hillinitial.hide()

		# simulated annieling radio
		self.saTemp = QtWidgets.QLabel(self.groupBox_2)
		self.saTemp.setGeometry(QtCore.QRect(10, 20, 91, 16))
		self.saTemp.setObjectName("saTemp")
		self.saTemp.setText("Temperature :")
		self.saTemp.hide()

		self.saTempVal = QtWidgets.QLineEdit(self.groupBox_2)
		self.saTempVal.setGeometry(QtCore.QRect(100, 20, 91, 20))
		self.saTempVal.setObjectName("saTempVal")
		self.saTempVal.setText("100")
		self.saTempVal.hide()

		self.saCool = QtWidgets.QLabel(self.groupBox_2)
		self.saCool.setGeometry(QtCore.QRect(10, 50, 81, 16))
		self.saCool.setObjectName("hillabel")
		self.saCool.setText("Cooling Rate :")
		self.saCool.hide()

		self.saCoolVal = QtWidgets.QLineEdit(self.groupBox_2)
		self.saCoolVal.setGeometry(QtCore.QRect(100, 50, 91, 20))
		self.saCoolVal.setObjectName("saCoolVal")
		self.saCoolVal.setText("0.997")
		self.saCoolVal.hide()

		self.speed = QtWidgets.QLabel(self.groupBox_2)
		self.speed.setGeometry(QtCore.QRect(10, 80, 91, 16))
		self.speed.setObjectName("label12")
		self.speed.setText("Speed: ")
		# self.Choice.clicked.connect(self.stop)
		self.speed_val = QtWidgets.QDoubleSpinBox(self.groupBox_2)
		self.speed_val.setGeometry(QtCore.QRect(100, 80, 91, 20))
		self.speed_val.setObjectName("Speed")
		self.speed_val.setMinimum(0)
		self.speed_val.setMaximum(2)
		self.speed_val.setSingleStep(0.01)

		self.energy = QtWidgets.QLabel(self.frame_2)
		self.energy.setGeometry(QtCore.QRect(10, 393, 91, 21))
		self.energy.setObjectName("label11")
		self.energy.setText("Energy: ")
		self.energy.hide()
		# self.Choice.clicked.connect(self.stop)
		self.energy_val = QtWidgets.QLineEdit(self.frame_2)
		self.energy_val.setGeometry(QtCore.QRect(110, 395, 101, 21))
		self.energy_val.setObjectName("Energy")
		self.energy_val.setEnabled(False)
		self.energy_val.hide()

		self.status = QtWidgets.QLabel(self.frame_2)
		self.status.setGeometry(QtCore.QRect(20, 423, 40, 13))
		self.status.setObjectName("status")
		self.status.setText("Status:")

		self.statusVal = QtWidgets.QLineEdit(self.frame_2)
		self.statusVal.setGeometry(QtCore.QRect(70, 420, 140, 20))
		self.statusVal.setObjectName("status")
		#self.statusVal.setText("Waiting...")
		self.statusVal.setEnabled(False)
		self.statusVal.setStyleSheet("color: Green;")


		self.pushButton = QtWidgets.QPushButton(self.frame_2)
		self.pushButton.setGeometry(QtCore.QRect(10, 450, 75, 23))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.pushButton.setFont(font)
		self.pushButton.setAutoFillBackground(False)
		self.pushButton.setStyleSheet("")
		self.pushButton.setObjectName("pushButton")
		self.pushButton.setText("Play")
		self.pushButton.clicked.connect(self.Start)
		self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_2.setGeometry(QtCore.QRect(10, 480, 75, 23))
		self.pushButton_2.setObjectName("pushButton_2")
		self.pushButton_2.setText("Restart")
		self.pushButton_2.clicked.connect(self.generateNqueen)

		self.previousBut = QtWidgets.QPushButton(self.frame_2)
		self.previousBut.setGeometry(QtCore.QRect(85, 480, 75, 23))
		self.previousBut.setObjectName("previousBut")
		self.previousBut.setText("Previous Step")
		self.previousBut.clicked.connect(self.prevStep)

		self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_3.setGeometry(QtCore.QRect(10, 510, 75, 23))
		self.pushButton_3.setObjectName("pushButton_3")
		self.pushButton_3.setText("Step")
		self.pushButton_3.clicked.connect(self.step)
		self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_5.setGeometry(QtCore.QRect(85, 510, 75, 23))
		self.pushButton_5.setObjectName("pushButton_5")
		self.pushButton_5.setText("Stop")
		self.pushButton_5.clicked.connect(self.stop)

		self.Choice = QtWidgets.QLabel(self.frame_2)
		self.Choice.setGeometry(QtCore.QRect(10, 370, 91, 21))
		self.Choice.setObjectName("pushButton_5")
		self.Choice.setText("Probability %:")
		#self.Choice.clicked.connect(self.stop)
		self.ChoiceVal = QtWidgets.QLineEdit(self.frame_2)
		self.ChoiceVal.setGeometry(QtCore.QRect(110, 370, 101, 21))
		self.ChoiceVal.setObjectName("ChoiceVal")
		self.ChoiceVal.setEnabled(False)
		self.Choice.hide()
		self.ChoiceVal.hide()
		#self.ChoiceVal.clicked.connect(self.stop)

		self.spinBox = QtWidgets.QSpinBox(self.frame_2)
		self.spinBox.setGeometry(QtCore.QRect(100, 20, 41, 22))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(9)
		font.setBold(True)
		font.setUnderline(False)
		font.setWeight(75)
		font.setStrikeOut(False)
		font.setKerning(False)
		self.spinBox.setFont(font)
		self.spinBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
		self.spinBox.setMinimum(4)
		self.spinBox.setMaximum(15)
		self.spinBox.setObjectName("spinBox")


		# layout.addWidget(QPushButton('1'), 0, 0)

		#label.resize(200,200)
		#label.setPixmap(pixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatio))
		label = QLabel()
		pixmap = QPixmap('queen2.png')
		label.setPixmap(pixmap)
		label.setStyleSheet("background: red")
		label2 = label


		#self.resize(pixmap.width(),pixmap.height())


		self.layout.setSpacing(0)


		# layout.addWidget(Color('white'), 0, 0)
		# label.setPixmap(pixmap)
		# layout.addWidget(Color('darkRed'), 0, 1)
		# layout.addWidget(Color('white'), 0, 2)
		# layout.addWidget(Color('darkRed'), 1, 0)
		# layout.addWidget(label, 1, 1)
		# layout.addWidget(label2, 1, 2)
		# layout.addWidget(label, 2, 0)
		# layout.addWidget(label2, 2, 1)
		# layout.addWidget(label, 2, 2)


		self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_4.setGeometry(QtCore.QRect(150, 20, 61, 23))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.pushButton_4.setFont(font)
		self.pushButton_4.setAutoFillBackground(False)
		self.pushButton_4.setStyleSheet("")
		self.pushButton_4.setObjectName("pushButton_4")
		self.pushButton_4.setText("Generate")
		self.pushButton_4.clicked.connect(self.generateNqueen)
		self.frame_2.raise_()
		self.frame.raise_()
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		
		# self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.Cover = QtWidgets.QFrame(self.centralwidget)
		self.Cover.setEnabled(True)
		self.Cover.setGeometry(QtCore.QRect(10, 10, 541, 541))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(9)
		sizePolicy.setHeightForWidth(self.Cover.sizePolicy().hasHeightForWidth())
		self.Cover.setSizePolicy(sizePolicy)
		self.Cover.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.Cover.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.Cover.setLineWidth(5)
		self.Cover.setObjectName("Cover")
		self.groupBox_4 = QtWidgets.QGroupBox(self.Cover)
		self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 521, 531))
		self.groupBox_4.setObjectName("groupBox_4")
		self.groupBox_4.setTitle("N-Queen")
		self.Cover.raise_()


		# genetics

		self.layout2 = QGridLayout()
		self.groupBox_4.setLayout(self.layout2)
		self.layout2.setSpacing(0)


	# overlaping frame 3
		self.frame_3 = QtWidgets.QFrame(self.centralwidget)
		self.frame_3.setGeometry(QtCore.QRect(10, 10, 541, 551))
		self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_3.setLineWidth(1)
		self.frame_3.setObjectName("frame_3")
		self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
		self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 541, 541))
		self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
		self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
		self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.groupBox_4 = QtWidgets.QGroupBox(self.gridLayoutWidget_2)
		self.groupBox_4.setObjectName("groupBox_4")
		self.groupBox_4.setTitle("Gen 2")
		self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_4)
		self.gridLayoutWidget_4.setGeometry(QtCore.QRect(9, 20, 251, 241))
		self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
		self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
		self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_4.setObjectName("gridLayout_4")
		self.gridLayout_2.addWidget(self.groupBox_4, 0, 1, 1, 1)

		self.groupBox_7 = QtWidgets.QGroupBox(self.gridLayoutWidget_2)
		self.groupBox_7.setObjectName("groupBox_7")
		self.groupBox_7.setTitle("Gen 1")
		self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_7)
		self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 251, 241))
		self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
		self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
		self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_3.setObjectName("gridLayout_3")
		self.gridLayout_2.addWidget(self.groupBox_7, 0, 0, 1, 1)
		self.groupBox_5 = QtWidgets.QGroupBox(self.gridLayoutWidget_2)
		self.groupBox_5.setObjectName("groupBox_5")
		self.groupBox_5.setTitle("Gen 3")
		self.gridLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_5)
		self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 251, 241))
		self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
		self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
		self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_5.setObjectName("gridLayout_5")
		self.gridLayout_2.addWidget(self.groupBox_5, 1, 0, 1, 1)
		self.groupBox_6 = QtWidgets.QGroupBox(self.gridLayoutWidget_2)
		self.groupBox_6.setObjectName("groupBox_6")
		self.groupBox_6.setTitle("Gen 4")
		self.gridLayoutWidget_6 = QtWidgets.QWidget(self.groupBox_6)
		self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 20, 251, 241))
		self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
		self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
		self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_6.setObjectName("gridLayout_6")
		self.gridLayout_2.addWidget(self.groupBox_6, 1, 1, 1, 1)

		# over lapping fram 4
		self.frame_4 = QtWidgets.QFrame(self.centralwidget)
		self.frame_4.setGeometry(QtCore.QRect(10, 10, 541, 551))
		self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_4.setLineWidth(1)
		self.frame_4.setObjectName("frame_4")
		self.gridLayoutWidget_21 = QtWidgets.QWidget(self.frame_4)
		self.gridLayoutWidget_21.setGeometry(QtCore.QRect(0, 0, 541, 541))
		self.gridLayoutWidget_21.setObjectName("gridLayoutWidget_21")
		self.gridLayout_21 = QtWidgets.QGridLayout(self.gridLayoutWidget_21)
		self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_21.setObjectName("gridLayout_21")
		self.groupBox_41 = QtWidgets.QGroupBox(self.gridLayoutWidget_21)
		self.groupBox_41.setObjectName("groupBox_41")
		self.gridLayoutWidget_41 = QtWidgets.QWidget(self.groupBox_41)
		self.gridLayoutWidget_41.setGeometry(QtCore.QRect(9, 20, 251, 241))
		self.gridLayoutWidget_41.setObjectName("gridLayoutWidget_41")
		self.gridLayout_41 = QtWidgets.QGridLayout(self.gridLayoutWidget_41)
		self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_41.setObjectName("gridLayout_41")
		self.gridLayout_21.addWidget(self.groupBox_41, 0, 1, 1, 1)

		self.groupBox_71 = QtWidgets.QGroupBox(self.gridLayoutWidget_21)
		self.groupBox_71.setObjectName("groupBox_71")
		self.gridLayoutWidget_31 = QtWidgets.QWidget(self.groupBox_71)
		self.gridLayoutWidget_31.setGeometry(QtCore.QRect(10, 20, 251, 241))
		self.gridLayoutWidget_31.setObjectName("gridLayoutWidget_31")
		self.gridLayout_31 = QtWidgets.QGridLayout(self.gridLayoutWidget_31)
		self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_31.setObjectName("gridLayout_31")
		self.gridLayout_21.addWidget(self.groupBox_71, 0, 0, 1, 1)
		self.groupBox_51 = QtWidgets.QGroupBox(self.gridLayoutWidget_21)
		self.groupBox_51.setObjectName("groupBox_51")
		self.gridLayoutWidget_51 = QtWidgets.QWidget(self.groupBox_51)
		self.gridLayoutWidget_51.setGeometry(QtCore.QRect(10, 20, 251, 241))
		self.gridLayoutWidget_51.setObjectName("gridLayoutWidget_51")
		self.gridLayout_51 = QtWidgets.QGridLayout(self.gridLayoutWidget_51)
		self.gridLayout_51.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_51.setObjectName("gridLayout_51")
		self.gridLayout_21.addWidget(self.groupBox_51, 1, 0, 1, 1)
		self.groupBox_61 = QtWidgets.QGroupBox(self.gridLayoutWidget_21)
		self.groupBox_61.setObjectName("groupBox_61")
		self.gridLayoutWidget_61 = QtWidgets.QWidget(self.groupBox_61)
		self.gridLayoutWidget_61.setGeometry(QtCore.QRect(10, 20, 251, 241))
		self.gridLayoutWidget_61.setObjectName("gridLayoutWidget_61")
		self.gridLayout_61 = QtWidgets.QGridLayout(self.gridLayoutWidget_61)
		self.gridLayout_61.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_61.setObjectName("gridLayout_61")
		self.gridLayout_21.addWidget(self.groupBox_61, 1, 1, 1, 1)

		self.frame_3.raise_()
		self.frame_4.raise_()

		self.frame_3.hide()
		self.frame_4.hide()

		# gen 1
		self.gridLayout_3.setSpacing(0)
		self.gridLayout_31.setSpacing(0)
		# gen 2
		self.gridLayout_4.setSpacing(0)
		self.gridLayout_41.setSpacing(0)
		# gen 3
		self.gridLayout_5.setSpacing(0)
		self.gridLayout_51.setSpacing(0)
		# gen 4
		self.gridLayout_6.setSpacing(0)
		self.gridLayout_61.setSpacing(0)

		# def retranslateUi(self, MainWindow):
		# 	_translate = QtCore.QCoreApplication.translate
		# 	MainWindow.setWindowTitle(_translate("MainWindow", "Heuristic Algorithms"))
		# 	self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
		# 	self.groupBox.setTitle(_translate("MainWindow", "Algorithms"))
		# 	self.radioButton.setText(_translate("MainWindow", "Hill Climbing"))
		# 	self.radioButton_2.setText(_translate("MainWindow", "Simulated Annealing"))
		# 	self.radioButton_3.setText(_translate("MainWindow", "Genetic Algorithm"))
		# 	self.radioButton_4.setText(_translate("MainWindow", "Local Beam"))
		# 	self.label.setText(_translate("MainWindow", "Board Size (N) :"))
		# 	self.groupBox_2.setTitle(_translate("MainWindow", "Parameters"))
		# 	self.pushButton.setText(_translate("MainWindow", "Start"))
		# 	self.pushButton_2.setText(_translate("MainWindow", "Restart"))
		# 	self.pushButton_3.setText(_translate("MainWindow", "One Step"))
		# 	self.pushButton_4.setText(_translate("MainWindow", "Generate"))
		self._widget_list = []
		self._widget_list2 = []


		self._widget_list3 = []
		self._widget_list31 = []
		self._widget_list4= []
		self._widget_list41 = []
		self._widget_list5 = []
		self._widget_list51 = []
		self._widget_list6 = []
		self._widget_list61 = []

		self.sizes = [0,0,0]
	def generateNqueen(self):
		global boardcounter, sa_list, hilllists, hillcondition, localBoards, All_lists_genetic
		self.statusVal.setText("")
		if self.radioButton_4.isChecked():
			print('do genetic')
			#All_lists_genetic = list()
			self.generateGeNqueen()
		else:
			self.radioButton.setEnabled(True)
			self.radioButton_2.setEnabled(True)
			self.radioButton_3.setEnabled(True)
			self.radioButton_4.setEnabled(True)
			self.spinBox.setEnabled(True)


			boardcounter , sa_list = 0, list()
			hilllists, hillcondition = list(), False
			localBoards = list()
			All_lists_genetic = list()

			if len(self._widget_list)>0:
				for i in reversed(range(self.layout.count())):
					print("yoo")
					#self.layout.removeWidget(widget)
					widgetToRemove = self.layout.itemAt(i).widget()
					widgetToRemove.setParent(None)
					widgetToRemove.deleteLater()
			self._widget_list = [0]*(self.spinBox.value()**2)

			if len(self._widget_list2)>0:
				for i in reversed(range(self.layout2.count())):
					#self.layout.removeWidget(widget)
					widgetToRemove = self.layout2.itemAt(i).widget()
					widgetToRemove.setParent(None)
					widgetToRemove.deleteLater()

			self._widget_list2 = [0]*(self.spinBox.value()**2)

			# self._widget_list.append(0)
			# self._widget_list2.append(0)

			# generating
			counteri=0
			for index in range(self.spinBox.value()):
				counterj = 0
				for jndex in range(self.spinBox.value()):
					label = QLabel()
					label2 = QLabel()
					# image1 = QImage("queen_M2.png")
					# image1 = image1.scaled(QSize(150,150))
					pixmap = QPixmap("queen_M2.png")
					label2.setPixmap(pixmap)
					label.setScaledContents(True)
					label2.setScaledContents(True)
					if ((index + jndex) % 2 == 0):
						#mywidget = Color(238,213,173)
						label.setStyleSheet("background: rgba(238,213,173,1);")
						label2.setStyleSheet("background: rgba(238,213,173,1);")
						self.layout.addWidget(label2, index, jndex)
						self.layout2.addWidget(label, index, jndex)


						self._widget_list.append(label)
					else:
						#mywidget = Color(154, 92 ,55)
						label.setStyleSheet("background: rgba(154,92,55,1);")
						label2.setStyleSheet("background: rgba(154,92,55,1);")
						self.layout.addWidget(label2, index, jndex)
						self.layout2.addWidget(label, index, jndex)



					print("hereee")
					self._widget_list[counterj*self.spinBox.value()+counteri] = label2
					#self._widget_list.append(label2)
					#self._widget_list2.append(label)
					self._widget_list2[counterj*self.spinBox.value()+counteri] = label
					label.style()
					counterj += 1
				print("out")
				counteri += 1
			#self.sizes[0] = label.width()
			#self.sizes[1] = label.height()
			#self.sizes[2] = label.size()

	def cleaner(self,widgetlistx ,layoutx):
		if len(widgetlistx) > 0 :
			for i in reversed(range(layoutx.count())):
				widgetToRemove = layoutx.itemAt(i).widget()
				widgetToRemove.setParent(None)
				widgetToRemove.deleteLater
		widgetlistx = [0]*(self.spinBox.value()**2)
		return widgetlistx



	def generateGeNqueen(self):
		global All_lists_genetic, Gboardcounter
		self.groupBox_4.setStyleSheet("")
		self.groupBox_5.setStyleSheet("")
		self.groupBox_6.setStyleSheet("")
		self.groupBox_7.setStyleSheet("")
		self.groupBox_7.setTitle("Gen 1")
		self.groupBox_4.setTitle("Gen 2")
		self.groupBox_5.setTitle("Gen 3")
		self.groupBox_6.setTitle("Gen 4")
		# self.radioButton.setEnabled(True)
		# self.radioButton_2.setEnabled(True)
		# self.radioButton_3.setEnabled(True)
		# self.radioButton_4.setEnabled(True)
		# self.spinBox.setEnabled(True)
		# self.statusVal.setText("")
		# global boardcounter, sa_list, hilllists, hillcondition, localBoards, All_lists_genetic
		# boardcounter , sa_list = 0, list()
		# hilllists, hillcondition = list(), False
		# localBoards = list()
		All_lists_genetic = list()
		Gboardcounter = 0
		#self._widget_list3 = [0]*(self.spinBox.value()**2)

		self._widget_list3 = self.cleaner(self._widget_list3,self.gridLayout_3)
		self._widget_list31 = self.cleaner(self._widget_list31,self.gridLayout_31)
		self._widget_list4 = self.cleaner(self._widget_list4,self.gridLayout_4)
		self._widget_list41 = self.cleaner(self._widget_list41,self.gridLayout_41)
		self._widget_list5 = self.cleaner(self._widget_list5,self.gridLayout_5)
		self._widget_list51 = self.cleaner(self._widget_list51,self.gridLayout_51)
		self._widget_list6 = self.cleaner(self._widget_list6,self.gridLayout_6)
		self._widget_list61 = self.cleaner(self._widget_list61,self.gridLayout_61)


		# generating
		counteri=0
		for index in range(self.spinBox.value()):
			counterj = 0
			for jndex in range(self.spinBox.value()):
				label = QLabel()
				label2 = QLabel()
				label3 = QLabel()
				label4 = QLabel()
				label1 = QLabel()
				label21 = QLabel()
				label31 = QLabel()
				label41 = QLabel()
				# image1 = QImage("queen_M2.png")
				# image1 = image1.scaled(QSize(150,150))
				pixmap = QPixmap("queen_M2.png")
				label.setPixmap(pixmap)
				label2.setPixmap(pixmap)
				label3.setPixmap(pixmap)
				label4.setPixmap(pixmap)

				label.setScaledContents(True)
				label2.setScaledContents(True)
				label3.setScaledContents(True)
				label4.setScaledContents(True)

				label1.setScaledContents(True)
				label21.setScaledContents(True)
				label31.setScaledContents(True)
				label41.setScaledContents(True)

				if ((index + jndex) % 2 == 0):
					#mywidget = Color(238,213,173)
					label.setStyleSheet("background: rgba(238,213,173,1);")
					label2.setStyleSheet("background: rgba(238,213,173,1);")
					label3.setStyleSheet("background: rgba(238,213,173,1);")
					label4.setStyleSheet("background: rgba(238,213,173,1);")

					# base
					self.gridLayout_4.addWidget(label2, index, jndex)
					self.gridLayout_5.addWidget(label, index, jndex)
					self.gridLayout_3.addWidget(label3, index, jndex)
					self.gridLayout_6.addWidget(label4, index, jndex)

					label1.setStyleSheet("background: rgba(238,213,173,1);")
					label21.setStyleSheet("background: rgba(238,213,173,1);")
					label31.setStyleSheet("background: rgba(238,213,173,1);")
					label41.setStyleSheet("background: rgba(238,213,173,1);")
					# cover
					self.gridLayout_31.addWidget(label1,index,jndex)
					self.gridLayout_41.addWidget(label21,index,jndex)
					self.gridLayout_51.addWidget(label31,index,jndex)
					self.gridLayout_61.addWidget(label41,index,jndex)


					#self._widget_list.append(label)
				else:
					#mywidget = Color(154, 92 ,55)
					label.setStyleSheet("background: rgba(154,92,55,1);")
					label2.setStyleSheet("background: rgba(154,92,55,1);")
					label3.setStyleSheet("background: rgba(154,92,55,1);")
					label4.setStyleSheet("background: rgba(154,92,55,1);")

					# base
					self.gridLayout_4.addWidget(label2, index, jndex)
					self.gridLayout_5.addWidget(label, index, jndex)
					self.gridLayout_3.addWidget(label3, index, jndex)
					self.gridLayout_6.addWidget(label4, index, jndex)

					label1.setStyleSheet("background: rgba(154,92,55,1);")
					label21.setStyleSheet("background: rgba(154,92,55,1);")
					label31.setStyleSheet("background: rgba(154,92,55,1);")
					label41.setStyleSheet("background: rgba(154,92,55,1);")

					# cover
					self.gridLayout_31.addWidget(label1,index,jndex)
					self.gridLayout_41.addWidget(label21,index,jndex)
					self.gridLayout_51.addWidget(label31,index,jndex)
					self.gridLayout_61.addWidget(label41,index,jndex)




				print("hereee")

				location = counterj*self.spinBox.value()+counteri
				#print(location," ", len(self._widget_list3))

				# first gen
				self._widget_list3[location] = label3
				self._widget_list31[location] = label1
				# second gen
				self._widget_list4[location] = label2
				self._widget_list41[location] = label21
				# third gen
				self._widget_list5[location] =label3
				self._widget_list51[location] = label31
				# fifth gen
				self._widget_list6[location] =label4
				self._widget_list61[location] = label41

				#self._widget_list[location] = label2
				#self._widget_list.append(label2)
				#self._widget_list2.append(label)
				#self._widget_list2[location] = label
				label.style()
				counterj += 1
			print("out")
			counteri += 1

	def Start(self):
		global sa_list, stop_it

		#self.generateNqueen()

		# hill climbing
		if self.radioButton.isChecked():
			stop_it = False
			#for i in sa_list and not stop_it:
			for i in hilllists :
				#t1 = threading.Thread(target=self.step)
				#t1.start()
				self.step()
				QApplication.processEvents()
				#t1.join()
				time.sleep(self.speed_val.value())
				if stop_it:
					break
				print("running")

			# condition, nl, lists = Hill.hillStart(self.hillinitial.value(),self.spinBox.value(),self.checkbox.isChecked())
			# print(nl)
			# counter = 0
			# for i in nl:
			# 	#if ((counter + 4) % 2 == 0):
			# 	i = i - 1
			# 	if not i<0:
			# 		self._widget_list2[i+counter*self.spinBox.value()].setStyleSheet("background: rgba(238,213,173,0.01);")
			# 	counter += 1


		# local beam
		if self.radioButton_2.isChecked():

			stop_it = False
			#for i in sa_list and not stop_it:
			for i in localBoards :
				#t1 = threading.Thread(target=self.step)
				#t1.start()
				self.step()
				QApplication.processEvents()
				#t1.join()
				time.sleep(self.speed_val.value())
				if stop_it:
					break
				print("running")

			print("local beam")
		# simulated annieling
		if self.radioButton_3.isChecked():
			# capture int - text exception
			print("Simulated annieling ")
			# print(f" hi my name is baty5 {self.saCoolVal.text()} and my number is {float(self.saCoolVal.text())}")
			#
			# sa_list = SA.startAnnealing(self.spinBox.value() , int(self.saTempVal.text()) ,float(self.saCoolVal.text()))
			# counter = 0
			# for i in sa_list[len(sa_list)-1]:
			# 	row = sa_list[len(sa_list)-1][counter].row
			#
			# 	#if not i<0:
			# 	self._widget_list2[row+counter*self.spinBox.value()].setStyleSheet("background: rgba(238,213,173,0.01);")
			# 	counter += 1
			# print(sa_list[len(sa_list)-1][1].row)
			stop_it = False
			#for i in sa_list and not stop_it:
			for i in sa_list :
				#t1 = threading.Thread(target=self.step)
				#t1.start()
				self.step()
				QApplication.processEvents()
				#t1.join()
				time.sleep(self.speed_val.value())
				if stop_it:
					break
				print("running")

		if self.radioButton_4.isChecked():
			stop_it = False
			#for i in sa_list and not stop_it:
			for i in All_lists_genetic :
				#t1 = threading.Thread(target=self.step)
				#t1.start()
				self.step()
				QApplication.processEvents()
				#t1.join()
				time.sleep(self.speed_val.value())
				if stop_it:
					break
				print("running")

			print("genetic")
	def prevStep(self):
		global  boardcounter, Gboardcounter, prev
		if( self.radioButton.isChecked() or self.radioButton_2.isChecked() or self.radioButton_3.isChecked() )and boardcounter>1:
			boardcounter -= 2
			prev = True
			self.step()
			prev = False
		elif self.radioButton_4.isChecked()and Gboardcounter>1:
			Gboardcounter -= 2
			prev = True
			self.step()
			prev = False

	def step(self):
		global sa_list, boardcounter, choicePerc, energy_list
		global hilllists, hillcondition
		global localBoards, localCondition
		global geneticcondition, All_lists_genetic , solGen, Gboardcounter

		# Hill climbing
		if self.radioButton.isChecked():
			print(len(hilllists))
			if len(hilllists) == 0:
				hillcondition, nl, hilllists = Hill.hillStart(self.hillinitial.value(),self.spinBox.value(),self.checkbox.isChecked())
				print(nl)
				counter = 0
				for i in hilllists[boardcounter]:
					i = i - 1
					if not i < 0:
						location = i+counter*self.spinBox.value()
						color = self._widget_list2[location].styleSheet()
						if "154" in color:
							self._widget_list2[location].setStyleSheet("background: rgba(154,92,55,0.01);")
						else:
							self._widget_list2[location].setStyleSheet("background: rgba(238,213,173,0.01);")
						#self._widget_list2[location].setStyleSheet("background: rgba(238,213,173,0.01);")
					counter += 1
				boardcounter += 1
			elif boardcounter < len(hilllists):
				if hillcondition == False:
					self.statusVal.setStyleSheet("color: red;")
					self.statusVal.setText("Unsolvable")
				else:
					self.statusVal.setStyleSheet("color: green;")
					self.statusVal.setText("Solvable")
				print('in')
				# cleaning
				# for i in self._widget_list2:
				#
				# 	color = i.styleSheet()
				# 	if "154" in color:
				# 		i.setStyleSheet("background: rgba(154,92,55,1);")
				# 	else:
				# 		i.setStyleSheet("background: rgba(238,213,173,1);")
				# cleaning 2
				counter = 0
				if prev:
					clean_target = boardcounter + 1
				else:
					clean_target = boardcounter - 1
				for i in hilllists[clean_target]:
					i = i - 1
					if not i < 0:
						location = i+counter*self.spinBox.value()
						color = self._widget_list2[location].styleSheet()
						if "154" in color:
							self._widget_list2[location].setStyleSheet("background: rgba(154,92,55,1);")
						else:
							self._widget_list2[location].setStyleSheet("background: rgba(238,213,173,1);")
					#self._widget_list2[location].setStyleSheet("background: rgba(238,213,173,0.01);")
					counter += 1

				counter = 0
				for i in hilllists[boardcounter]:
					i = i - 1
					if not i < 0:
						location = i+counter*self.spinBox.value()
						color = self._widget_list2[location].styleSheet()
						if "154" in color:
							self._widget_list2[location].setStyleSheet("background: rgba(154,92,55,0.01);")
						else:
							self._widget_list2[location].setStyleSheet("background: rgba(238,213,173,0.01);")
					counter += 1
				boardcounter += 1





	# for i in nl:
		# 		#if ((counter + 4) % 2 == 0):
		# 		i = i - 1
		# 		if not i<0:
		# 			self._widget_list2[i+counter*self.spinBox.value()].setStyleSheet("background: rgba(238,213,173,0.01);")
		# 		counter += 1


		# simulated annieling
		if self.radioButton_3.isChecked():

			if len(sa_list) == 0:
				sa_list, choicePerc, energy_list = SA.startAnnealing(self.spinBox.value(), int(self.saTempVal.text()), float(self.saCoolVal.text()))
				counter = 0
				for i in sa_list[0]:

					print("heeere")
					print(type(i))
					row = i.row
					#print(row)
					#if not i<0:
					location = row+counter*self.spinBox.value()
					color = self._widget_list2[location].styleSheet()
					color = color[:-3] + "0.01);"
					#print(color)
					self._widget_list2[location].setStyleSheet(color)
					counter += 1
				print("there", choicePerc[boardcounter])

				self.ChoiceVal.setText(str(round(choicePerc[boardcounter],8)))
				self.energy_val.setText(str(energy_list[boardcounter]))
				boardcounter += 1
			elif boardcounter < len(sa_list):

				# cleaning
				counter = 0
				for i in self._widget_list2:

					color = i.styleSheet()
					if "154" in color:
						i.setStyleSheet("background: rgba(154,92,55,1);")
					else:
						i.setStyleSheet("background: rgba(238,213,173,1);")

						#print(color)
					# row = queen.row
					# location = row+counter*self.spinBox.value()
					# color = self._widget_list2[location].styleSheet()
					# print(color, "cleaning")
					# color = color[:30] + "1);"
					# print(color, "cleaning2")
					# self._widget_list2[location].setStyleSheet(color)


					counter += 1
				# re drawing
				counter = 0
				for queen in sa_list[boardcounter]:
					row = queen.row
					location = row+counter*self.spinBox.value()
					#if not i<0:
					color = self._widget_list2[location].styleSheet()
					if "154" in color:
						self._widget_list2[location].setStyleSheet("background: rgba(154,92,55,0.01);")
					else:
						self._widget_list2[location].setStyleSheet("background: rgba(238,213,173,0.01);")
					print(color)
					#self._widget_list2[row+counter*self.spinBox.value()].setStyleSheet(color)
					counter += 1
					print(choicePerc[boardcounter])
				self.ChoiceVal.setText(str(round(choicePerc[boardcounter],8)))
				self.energy_val.setText(str(energy_list[boardcounter]))
			boardcounter += 1

		# local beam
		if self.radioButton_2.isChecked():
			print("Local Beam")
			if len(localBoards) == 0 :
				boards, localCondition = LB.localbeamStart(self.spinBox.value())
				localBoards = boards
				counter = 0
				for i in localBoards[0]:
					i = i - 1
					location = i+counter*self.spinBox.value()
					color = self._widget_list2[location].styleSheet()
					if "154" in color:
						self._widget_list2[location].setStyleSheet("background: rgba(154,92,55,0.01);")
					else:
						self._widget_list2[location].setStyleSheet("background: rgba(238,213,173,0.01);")

					counter += 1
				boardcounter += 1
				print("there")


			elif boardcounter < len(localBoards):
				if localCondition == False:
					self.statusVal.setStyleSheet("color: red;")
					self.statusVal.setText("Unsolvable")
				for i in self._widget_list2:

					color = i.styleSheet()
					if "154" in color:
						i.setStyleSheet("background: rgba(154,92,55,1);")
					else:
						i.setStyleSheet("background: rgba(238,213,173,1);")
				counter = 0

				for i in localBoards[boardcounter]:
					i = i - 1
					location = i+counter*self.spinBox.value()
					color = self._widget_list2[location].styleSheet()
					if "154" in color:
						self._widget_list2[location].setStyleSheet("background: rgba(154,92,55,0.01);")
					else:
						self._widget_list2[location].setStyleSheet("background: rgba(238,213,173,0.01);")
					counter += 1
				boardcounter += 1

			elif localCondition == True:
				self.statusVal.setStyleSheet("color: Green;")
				self.statusVal.setText("Finished and solved")

		# genetic
		if self.radioButton_4.isChecked():
			print("Genetic algorithm")
			if len(All_lists_genetic) == 0:
				geneticcondition, solGen, All_lists_genetic = GN.Genetic_Algorithm(self.spinBox.value())
				print(All_lists_genetic)
				#print(len(All_lists_genetic))
				#print(All_lists_genetic[0])
				#print(All_lists_genetic[0][0])
				counter = 0
				for generation in All_lists_genetic[Gboardcounter]:
					# participants 1
					print(generation, end="")

					print()
					if counter == 0:
						self.geneticIteratior(generation,self._widget_list31,0.01)
						if generation == solGen:
							self.groupBox_7.setTitle("Gen 1 ( Solution)")
							self.groupBox_7.setStyleSheet("color: Green")
					if counter == 1:
						self.geneticIteratior(generation,self._widget_list41,0.01)
						if generation == solGen:
							self.groupBox_4.setTitle("Gen 2 ( Solution)")
							self.groupBox_4.setStyleSheet("color: Green")
					if counter == 2:
						self.geneticIteratior(generation,self._widget_list51,0.01)
						if generation == solGen:
							self.groupBox_5.setTitle("Gen 3 ( Solution)")
							self.groupBox_5.setStyleSheet("color: Green")
					if counter == 3:
						self.geneticIteratior(generation,self._widget_list61,0.01)
						if generation == solGen:
							self.groupBox_6.setTitle("Gen 4 ( Solution)")
							self.groupBox_6.setStyleSheet("color: Green")
					counter += 1
				Gboardcounter += 1
			elif Gboardcounter<len(All_lists_genetic):
				if geneticcondition:
					self.statusVal.setStyleSheet("color: Green;")
					self.statusVal.setText("solvable")
				# cleaning
				counter = 0
				if prev:
					clean_target = Gboardcounter + 1
				else:
					clean_target = Gboardcounter-1
				for generation in All_lists_genetic[clean_target]:
					if counter == 0:
						self.geneticIteratior(generation,self._widget_list31,1)
					if counter == 1:
						self.geneticIteratior(generation,self._widget_list41,1)
					if counter == 2:
						self.geneticIteratior(generation,self._widget_list51,1)
					if counter == 3:
						self.geneticIteratior(generation,self._widget_list61,1)
					counter +=1

				print("after cleaning")
				counter = 0
				for generation in All_lists_genetic[Gboardcounter]:
					print(generation, end="")
					print()
					if counter == 0:
						self.geneticIteratior(generation,self._widget_list31,0.01)
						if generation == solGen:
							self.groupBox_7.setTitle("Gen 1 ( Solution)")
							self.groupBox_7.setStyleSheet("color: Green")
					if counter == 1:
						self.geneticIteratior(generation,self._widget_list41,0.01)
						if generation == solGen:
							self.groupBox_4.setTitle("Gen 2 ( Solution)")
							self.groupBox_4.setStyleSheet("color: Green")
					if counter == 2:
						self.geneticIteratior(generation,self._widget_list51,0.01)
						if generation == solGen:
							self.groupBox_5.setTitle("Gen 3 ( Solution)")
							self.groupBox_5.setStyleSheet("color: Green")
					if counter == 3:
						self.geneticIteratior(generation,self._widget_list61,0.01)
						if generation == solGen:
							self.groupBox_6.setTitle("Gen 4 ( Solution)")
							self.groupBox_6.setStyleSheet("color: Green")
					counter += 1
				Gboardcounter += 1



		print("step")

	def geneticIteratior(self, generation,layoutx, opacity):
		counter = 0
		print(f"doing gen { generation}")
		for i in generation:
			i = i - 1

			location = i+counter*self.spinBox.value()
			color = layoutx[location].styleSheet()
			if "154" in color:
				layoutx[location].setStyleSheet(f"background: rgba(154,92,55,{opacity});")
			else:
				layoutx[location].setStyleSheet(f"background: rgba(238,213,173,{opacity});")
			#self._widget_list2[location].setStyleSheet("background: rgba(238,213,173,0.01);")
			counter += 1

	def stop(self):
		global stop_it

		stop_it = True
		#self.Cover.hide()
		#self.frame.hide()




	def hillOptions(self):
		if self.radioButton.isChecked():
			self.checkbox.show()
			self.hillabel.show()
			self.hillinitial.show()
			self.hillinitial.setMaximum(self.spinBox.value())
		else:
			self.checkbox.hide()
			self.hillabel.hide()
			self.hillinitial.hide()

	def saOptions(self):
		if self.radioButton_3.isChecked():
			self.saCool.show()
			self.saTemp.show()
			self.saCoolVal.show()
			self.saTempVal.show()
			#self._widget_list2[self.spinBox.value()].setStyleSheet("background: rgba(154, 92 ,55, 1);")
			self.Choice.show()
			self.ChoiceVal.show()
			self.energy_val.show()
			self.energy.show()
		else:
			self.saCool.hide()
			self.saTemp.hide()
			self.saCoolVal.hide()
			self.saTempVal.hide()
			self.Choice.hide()
			self.ChoiceVal.hide()
			self.energy_val.hide()
			self.energy.hide()

	def locOptions(self):
		print("local")


	def geOptions(self):
		if self.radioButton_4.isChecked():
			self.frame.hide()
			self.Cover.hide()
			self.frame_3.show()
			self.frame_4.show()
			self.generateGeNqueen()
		else:
			self.frame.show()
			self.Cover.show()
			self.frame_3.hide()
			self.frame_4.hide()


if __name__ == "__main__":
	import sys
	
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
