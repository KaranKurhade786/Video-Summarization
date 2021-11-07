# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/gui/newUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(372, 525)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(253, 248, 245);\n"
"color: rgb(221, 175, 148);")
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 372, 471))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.selectframe = QtWidgets.QFrame(self.layoutWidget)
        self.selectframe.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"border-bottom-width: 1px;\n"
"border-bottom-style: outset;\n"
"border-bottom-color: rgb(79, 72, 70);")
        self.selectframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.selectframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.selectframe.setObjectName("selectframe")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.selectframe)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.selectLabel = QtWidgets.QLabel(self.selectframe)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        self.selectLabel.setFont(font)
        self.selectLabel.setStyleSheet("border-style: None;\n"
"")
        self.selectLabel.setObjectName("selectLabel")
        self.horizontalLayout_5.addWidget(self.selectLabel)
        self.selectComboBox = QtWidgets.QComboBox(self.selectframe)
        self.selectComboBox.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"selection-background-color: rgb(247, 247, 247);\n"
"selection-color: rgb(221, 175, 148);\n"
"")
        self.selectComboBox.setObjectName("selectComboBox")
        self.selectComboBox.addItem("")
        self.selectComboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.selectComboBox)
        self.verticalLayout.addWidget(self.selectframe)
        self.chooseFrame = QtWidgets.QFrame(self.layoutWidget)
        self.chooseFrame.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"border-bottom-width: 1px;\n"
"border-bottom-style: outset;\n"
"border-bottom-color: rgb(79, 72, 70);")
        self.chooseFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chooseFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chooseFrame.setObjectName("chooseFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.chooseFrame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.chooseLabel = QtWidgets.QLabel(self.chooseFrame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.chooseLabel.setFont(font)
        self.chooseLabel.setStyleSheet("border-style: None;\n"
"")
        self.chooseLabel.setObjectName("chooseLabel")
        self.horizontalLayout_6.addWidget(self.chooseLabel)
        self.chooseComboBox = QtWidgets.QComboBox(self.chooseFrame)
        self.chooseComboBox.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"selection-background-color: rgb(247, 247, 247);\n"
"selection-color: rgb(221, 175, 148);\n"
"")
        self.chooseComboBox.setObjectName("chooseComboBox")
        self.chooseComboBox.addItem("")
        self.chooseComboBox.addItem("")
        self.horizontalLayout_6.addWidget(self.chooseComboBox)
        self.verticalLayout.addWidget(self.chooseFrame)
        self.urlFrame = QtWidgets.QFrame(self.layoutWidget)
        self.urlFrame.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"border-bottom-width: 1px;\n"
"border-bottom-style: outset;\n"
"border-bottom-color: rgb(79, 72, 70);")
        self.urlFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.urlFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.urlFrame.setObjectName("urlFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.urlFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.urlLabel = QtWidgets.QLabel(self.urlFrame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.urlLabel.setFont(font)
        self.urlLabel.setStyleSheet("border-bottom-style: none;")
        self.urlLabel.setObjectName("urlLabel")
        self.horizontalLayout.addWidget(self.urlLabel)
        self.urlTextBox = QtWidgets.QLineEdit(self.urlFrame)
        self.urlTextBox.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.urlTextBox.setObjectName("urlTextBox")
        self.horizontalLayout.addWidget(self.urlTextBox)
        self.verticalLayout.addWidget(self.urlFrame)
        self.pathFrame = QtWidgets.QFrame(self.layoutWidget)
        self.pathFrame.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"border-bottom-width: 1px;\n"
"border-bottom-style: outset;\n"
"border-bottom-color: rgb(79, 72, 70);")
        self.pathFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pathFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pathFrame.setObjectName("pathFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.pathFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pathLabel = QtWidgets.QLabel(self.pathFrame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pathLabel.setFont(font)
        self.pathLabel.setStyleSheet("border-bottom-style: none;")
        self.pathLabel.setObjectName("pathLabel")
        self.horizontalLayout_2.addWidget(self.pathLabel)
        self.pathTextBox = QtWidgets.QLineEdit(self.pathFrame)
        self.pathTextBox.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pathTextBox.setObjectName("pathTextBox")
        self.horizontalLayout_2.addWidget(self.pathTextBox)
        self.browseButton = QtWidgets.QPushButton(self.pathFrame)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout_2.addWidget(self.browseButton)
        self.verticalLayout.addWidget(self.pathFrame)
        self.generateframe = QtWidgets.QFrame(self.layoutWidget)
        self.generateframe.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"border-bottom-width: 1px;\n"
"border-bottom-style: outset;\n"
"border-bottom-color: rgb(79, 72, 70);")
        self.generateframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.generateframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.generateframe.setObjectName("generateframe")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.generateframe)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.generateButton = QtWidgets.QPushButton(self.generateframe)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.generateButton.setFont(font)
        self.generateButton.setStyleSheet("")
        self.generateButton.setObjectName("generateButton")
        self.horizontalLayout_3.addWidget(self.generateButton)
        self.verticalLayout.addWidget(self.generateframe)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gifFrame = QtWidgets.QFrame(self.layoutWidget)
        self.gifFrame.setStyleSheet("")
        self.gifFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gifFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gifFrame.setObjectName("gifFrame")
        self.outputBox = QtWidgets.QLabel(self.gifFrame)
        self.outputBox.setGeometry(QtCore.QRect(0, 0, 361, 161))
        self.outputBox.setText("")
        self.outputBox.setObjectName("outputBox")
        self.verticalLayout_2.addWidget(self.gifFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 372, 26))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuOptions.addAction(self.actionExit)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Summarization"))
        self.selectLabel.setText(_translate("MainWindow", "SELECT"))
        self.selectComboBox.setPlaceholderText(_translate("MainWindow", "sumarization"))
        self.selectComboBox.setItemText(0, _translate("MainWindow", "Movie"))
        self.selectComboBox.setItemText(1, _translate("MainWindow", "Sports"))
        self.chooseLabel.setText(_translate("MainWindow", "Choose"))
        self.chooseComboBox.setPlaceholderText(_translate("MainWindow", "type of input"))
        self.chooseComboBox.setItemText(0, _translate("MainWindow", "Local Computer"))
        self.chooseComboBox.setItemText(1, _translate("MainWindow", "Youtube Link"))
        self.urlLabel.setText(_translate("MainWindow", "URL"))
        self.pathLabel.setText(_translate("MainWindow", "PATH"))
        self.browseButton.setText(_translate("MainWindow", "BROWSE"))
        self.generateButton.setText(_translate("MainWindow", "GENERATE"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))