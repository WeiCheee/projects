# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(373, 255)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 70, 81, 41))
        self.pushButton.setMaximumSize(QtCore.QSize(111, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setMouseTracking(False)
        self.comboBox.setTabletTracking(False)
        self.comboBox.setObjectName("comboBox")
        choice = ['1','2','3','4','5','6','7']
        for label in choice:
            self.comboBox.addItem(label)
            print(label)
#---------------------------設定物件位置與名稱--------------------------
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 180, 161, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.openGLWidget = QtWidgets.QTextEdit(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(190, 20, 151, 181))
        self.openGLWidget.setObjectName("openGLWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 373, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox.currentIndexChanged[str].connect(self.print_value) # 項目改變，則傳項目內容
        self.comboBox.currentIndexChanged[int].connect(self.print_value)  # 項目改變，則傳遞索引值
        self.pushButton.clicked.connect(self.call_event) # buttom1 event
        self.pushButton_2.clicked.connect(self.call_stop) # buttom call stop
       
    def print_value(self,i):
        self.selected = i

    def thread_jobs(self):
        print("----------------------------------------")    
        if(self.selected == '--version--'):
            self.kms_key(self.selected, self.cmd)
            print("please select a version for windows")
        else:
            self.windows_crash(self.selected, self.cmd, self)

    def call_event(self):    
        self.t = threading.Thread(target=self.thread_jobs, args=())
        self.t.start()
        # self.openGLWidget.clear()


    def call_stop(self):
        self.stop = 1
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Windows Crash"))
        self.pushButton.setText(_translate("MainWindow", "Active"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.comboBox.setCurrentText(_translate("MainWindow", " "))
        for index in range(0,len(list(self.kms.keys()))) :
            self.comboBox.setItemText(index, _translate("MainWindow", (list(self.kms.keys()))[index]))
