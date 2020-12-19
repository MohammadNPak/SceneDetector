# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\UI_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 782)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.movieDetailTableView = QtWidgets.QTableView(self.centralwidget)
        self.movieDetailTableView.setGeometry(QtCore.QRect(20, 10, 251, 451))
        self.movieDetailTableView.setMinimumSize(QtCore.QSize(0, 200))
        self.movieDetailTableView.setObjectName("movieDetailTableView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 600, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 600, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.ffmpegAddressBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ffmpegAddressBtn.setGeometry(QtCore.QRect(430, 600, 75, 23))
        self.ffmpegAddressBtn.setObjectName("ffmpegAddressBtn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 640, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 640, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.videoAddressBtn = QtWidgets.QPushButton(self.centralwidget)
        self.videoAddressBtn.setGeometry(QtCore.QRect(430, 640, 75, 23))
        self.videoAddressBtn.setObjectName("videoAddressBtn")
        self.startProcessBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startProcessBtn.setGeometry(QtCore.QRect(430, 690, 75, 23))
        self.startProcessBtn.setObjectName("startProcessBtn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(300, 20, 751, 441))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.videoPlayer = VideoPlayer(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoPlayer.sizePolicy().hasHeightForWidth())
        self.videoPlayer.setSizePolicy(sizePolicy)
        self.videoPlayer.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.videoPlayer.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 5px;")
        self.videoPlayer.setObjectName("videoPlayer")
        self.verticalLayout.addWidget(self.videoPlayer)
        self.mainProgressBar = QtWidgets.QProgressBar(self.widget)
        self.mainProgressBar.setProperty("value", 0)
        self.mainProgressBar.setObjectName("mainProgressBar")
        self.verticalLayout.addWidget(self.mainProgressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menufile.addAction(self.actionopen)
        self.menuEdit.addAction(self.actionPreferences)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.ffmpegAddressBtn.setText(_translate("MainWindow", "PushButton"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.videoAddressBtn.setText(_translate("MainWindow", "PushButton"))
        self.startProcessBtn.setText(_translate("MainWindow", "PushButton"))
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionopen.setShortcut(_translate("MainWindow", "Alt+O"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
from py.VideoPlayer import VideoPlayer
