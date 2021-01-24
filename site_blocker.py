# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# GUI for the first part of the site blocker (gets website names, time duration)

from PyQt5 import QtCore, QtGui, QtWidgets


def getWebsite(QTSite):
    return str(QTSite.toPlainText())


def readFile(fileName):
    websites = []
    try:
        websites_file = open(fileName, "r")
        for line in websites_file:
            line = line.split(",")
            settings = [line[0], line[1]]
            websites.append(settings)
    except IOError:
        websites = []
    return websites


def writeFile(settings, fileName):
    output = open(fileName, "w")
    for setting in settings:
        output.write(str(setting[0]) + "," + str(setting[1]) + "\n")
    output.close()


class Ui_MainWindow(object):
    def __init__(self):
        self.row = 6
        self.MainWindow = None

        self.siteNum = 1
        self.sites = []
        self.siteIndex = 0

        self.dbNum = 1
        self.deleteButton = []
        self.dbIndex = 0

        self.cbNum = 1
        self.checkBox = []
        self.cbIndex = 0

        self.website_list = readFile("siteNames.csv")

        self.settingsList = []

        # the first value in here is hour and second is minute
        self.time = []
        self.saveNum = 0
    def setupUi(self, MainWindow):
        # window set up
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.setDurationLabel = QtWidgets.QLabel(self.centralwidget)
        self.setDurationLabel.setGeometry(QtCore.QRect(300, 329, 141, 31))
        self.setDurationLabel.setObjectName("setDurationLabel")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(240, 359, 266, 63))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.durationGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.durationGridLayout.setContentsMargins(0, 0, 0, 0)
        self.durationGridLayout.setObjectName("durationGridLayout")
        self.minutesField = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.minutesField.setMaximumSize(QtCore.QSize(16777215, 31))
        self.minutesField.setObjectName("minutesField")
        self.durationGridLayout.addWidget(self.minutesField, 1, 1, 1, 1)
        self.minutesLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.minutesLabel.setObjectName("minutesLabel")
        self.durationGridLayout.addWidget(self.minutesLabel, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.hoursField = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.hoursField.setMaximumSize(QtCore.QSize(16777215, 31))
        self.hoursField.setObjectName("hoursField")
        self.durationGridLayout.addWidget(self.hoursField, 1, 0, 1, 1)
        self.hoursLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.hoursLabel.setObjectName("hoursLabel")
        self.durationGridLayout.addWidget(self.hoursLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(270, 40, 231, 51))
        self.titleLabel.setObjectName("titleLabel")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(320, 450, 111, 31))
        self.saveButton.setObjectName("saveButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(100, 100, 576, 200))  # size for scroll area
        self.scrollArea.setMaximumSize(QtCore.QSize(576, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 559, 136))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

        if len(self.website_list) > 0:
            i = 4
            for websiteToggle in self.website_list:
                self.createSite(i)
                self.createCheckBoxButton(i)
                self.createDelButton(i)
                self.sites[self.siteIndex - 1].setPlainText(websiteToggle[0])
                self.checkBox[self.cbIndex - 1].setChecked(bool(websiteToggle[1]))
                i += 1
        else:
            for i in range(4, 6):
                self.createSite(i)
                self.createCheckBoxButton(i)
                self.createDelButton(i)

        self.blockedLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blockedLabel.setObjectName("blockedLabel")
        self.gridLayout.addWidget(self.blockedLabel, 2, 1, 1, 1)
        self.addNewButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.addNewButton.setObjectName("addNewButton")
        self.gridLayout.addWidget(self.addNewButton, 2, 2, 1, 1)
        self.blockedSitesLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blockedSitesLabel.setObjectName("blockedSitesLabel")
        self.gridLayout.addWidget(self.blockedSitesLabel, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.setDurationLabel.setText(_translate("MainWindow",
                                                 "<html><head/><body><p align=\"center\"><span style=\" "
                                                 "font-size:24pt;\">Set Duration</span></p></body></html>"))
        self.minutesField.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                             "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta "
                                             "charset=\"utf-8\" /><style type=\"text/css\">\n "
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; "
                                             "font-size:13pt; font-weight:400; font-style:normal;\">\n "
                                             "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                             "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                             "-qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.minutesLabel.setText(_translate("MainWindow",
                                             "<html><head/><body><p align=\"center\"><span style=\" "
                                             "font-size:18pt;\">Minutes</span></p></body></html>"))
        self.hoursField.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                           "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta "
                                           "charset=\"utf-8\" /><style type=\"text/css\">\n "
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; "
                                           "font-size:13pt; font-weight:400; font-style:normal;\">\n "
                                           "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                           "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                           "text-indent:0px;\"><br /></p></body></html>"))
        self.hoursLabel.setText(_translate("MainWindow",
                                           "<html><head/><body><p align=\"center\"><span style=\" "
                                           "font-size:18pt;\">Hours</span></p></body></html>"))
        self.titleLabel.setText(_translate("MainWindow",
                                           "<html><head/><body><p align=\"center\"><span style=\" "
                                           "font-size:36pt;\">Web Blocker</span></p></body></html>"))
        self.saveButton.setText(_translate("MainWindow", "Save"))

        for button in self.deleteButton:
            button.setText(_translate("MainWindow", "Delete"))

        self.blockedLabel.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" "
                                             "font-size:18pt;\">Blocked</span></p></body></html>"))
        self.addNewButton.setText(_translate("MainWindow", "Add New"))
        self.blockedSitesLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" "
                                                                "font-size:18pt;\">Blocked "
                                                                "Sites</span></p></body></html>"))

    def connectActions(self):
        # Save Button Pressed
        self.saveButton.clicked.connect(self.saveClicked)

        # Add New Row
        self.addNewButton.clicked.connect(self.newRow)

    def saveClicked(self):
        if self.saveNum < 1:
            for i in range(len(self.sites)):
                link = getWebsite(self.sites[i])
                checked = self.checkBox[i].isChecked()
                if link != "":
                    self.settingsList.append([link, checked])
            writeFile(self.settingsList, "siteNames.csv")
            self.saveNum += 1
        else:
            print("was saved!")

    def newRow(self):
        print("adding new row...")

        # delete button
        self.createDelButton(self.row)

        # check box
        self.createCheckBoxButton(self.row)

        # sites
        self.createSite(self.row)

        self.row += 1

    def createSite(self, row):
        self.sites.append(QtWidgets.QTextEdit(self.scrollAreaWidgetContents))
        self.sites[self.siteIndex].setMinimumSize(QtCore.QSize(351, 31))
        self.sites[self.siteIndex].setMaximumSize(QtCore.QSize(351, 31))
        self.sites[self.siteIndex].setObjectName("site" + str(self.siteNum))
        self.gridLayout.addWidget(self.sites[self.siteIndex], row, 0, 1, 1)
        self.siteNum += 1
        self.siteIndex += 1

    def createCheckBoxButton(self, row):
        self.checkBox.append(QtWidgets.QCheckBox(self.scrollAreaWidgetContents))
        self.checkBox[self.cbIndex].setText("")
        self.checkBox[self.cbIndex].setObjectName("checkBox1")
        self.gridLayout.addWidget(self.checkBox[self.cbIndex], row, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.cbIndex += 1
        self.cbNum += 1

    def createDelButton(self, row):
        _translate = QtCore.QCoreApplication.translate
        self.deleteButton.append(QtWidgets.QPushButton(self.scrollAreaWidgetContents))
        self.deleteButton[self.dbIndex].setObjectName("deleteButton" + str(self.dbNum))
        self.deleteButton[self.dbIndex].setText(_translate("MainWindow", "Delete"))
        self.gridLayout.addWidget(self.deleteButton[self.dbIndex], row, 2, 1, 1)
        self.dbIndex += 1
        self.dbNum += 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.connectActions()
    MainWindow.show()
    sys.exit(app.exec_())
