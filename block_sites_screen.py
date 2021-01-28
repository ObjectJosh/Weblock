# GUI for the first part of the site blocker (gets website names, time duration)

from PyQt5 import QtCore, QtGui, QtWidgets
from survey_screen import UIWindow
import sys
import settings

def readFile(fileName):
    websites = []
    try:
        websites_file = open(fileName, "r")
        for line in websites_file:
            line = line.split(",")
            settings = [line[0], line[1]]
            websites.append(settings)
        websites_file.close()
    except IOError:
        websites = []
    return websites

def writeFile(settings, fileName):
    print("writing into the file")
    output = open(fileName, "w")
    for setting in settings:
        output.write(str(setting[0]) + "," + str(setting[1]) + "\n")
    output.close()

class Ui_MainWindow(object):
    def __init__(self):
        self.MainWindow = None
        # starting row
        self.row = 6
        # site
        self.siteNum = 1
        self.sites = []
        self.siteIndex = 0
        # delete button
        self.dbNum = 1
        self.deleteButton = []
        self.dbIndex = 0
        # checkbox
        self.cbNum = 1
        self.checkBox = []
        self.cbIndex = 0
        # time
        self.hour = 0
        self.minute = 0
        # website list
        self.website_list = []
        # list from data
        temp_list = readFile("data.csv")
        try:
            int(temp_list[-1][0])
            self.website_list = temp_list[:-1]
        except IndexError: 
            self.website_list = []
        except ValueError:
            self.website_list = temp_list
        # settings list
        self.settingsList = []
        # time: index 0 is hour, index 1 is minute
        self.time = []

    def file2(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = UIWindow()
        self.ui.setupUi(self.mainWindow)
        self.ui.connectActions(self.mainWindow)
        # self.ui.setHour(int(self.hour))
        # self.ui.setMinute(int(self.minute))
        self.mainWindow.show()

    def setupUi(self, MainWindow):
        # Window set up
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 630)
        window_width = int(self.MainWindow.frameGeometry().width())
        window_height = int(self.MainWindow.frameGeometry().height())
        MainWindow.setStyleSheet("background-color: #1961b2\n")
        # Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Set Duration Label (change this to move "Set Duration" label)
        self.setDurationLabel = QtWidgets.QLabel(self.centralwidget)
        self.setDurationLabel.setGeometry(QtCore.QRect((window_width / 2) - 70, (window_height / 2) + 50, 140, 30))
        self.setDurationLabel.setStyleSheet("color: #95bfe7")
        self.setDurationLabel.setObjectName("setDurationLabel")
        # Grid Layout for Sites (change this to move hour/minute text fields)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect((window_width / 2) - 133, (window_height / 2) + 50, 266, 64))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        # Grid Layout for Duration
        self.durationGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.durationGridLayout.setContentsMargins(0, 0, 0, 0)
        self.durationGridLayout.setObjectName("durationGridLayout")
        # Minutes Text Field
        self.minutesField = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.minutesField.setMaximumSize(QtCore.QSize(150, 30))
        self.minutesField.setStyleSheet("background-color: #c8daf2")
        self.minutesField.setObjectName("minutesField")
        self.durationGridLayout.addWidget(self.minutesField, 1, 1, 1, 1)
        # Minutes Label
        self.minutesLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.minutesLabel.setStyleSheet("color: #95bfe7")
        self.minutesLabel.setObjectName("minutesLabel")
        self.durationGridLayout.addWidget(self.minutesLabel, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        # Hours Text Field
        self.hoursField = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.hoursField.setMaximumSize(QtCore.QSize(150, 25))
        self.hoursField.setStyleSheet("background-color: #c8daf2")
        self.hoursField.setText("hello")
        self.hoursField.setPlainText("heloo")
        self.hoursField.setObjectName("hoursField")
        self.durationGridLayout.addWidget(self.hoursField, 1, 0, 1, 1)
        # Hours Label
        self.hoursLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.hoursLabel.setStyleSheet("color:     #95bfe7")
        self.hoursLabel.setObjectName("hoursLabel")
        self.durationGridLayout.addWidget(self.hoursLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        # Title Label: "Web Blocker"
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect((window_width / 2) - 120, (window_height / 2) - 270, 240, 50))
        self.titleLabel.setStyleSheet("color:     #95bfe7")
        self.titleLabel.setObjectName("titleLabel")
        # Save Button (change this to move the Save button)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect((window_width / 2) - 55, (window_height / 2) + 140, 110, 31))
        self.saveButton.setStyleSheet("background-color: #173364; color:     #c8daf2")
        self.saveButton.setObjectName("saveButton")
        # Scroll Area for Sites (change this to move sites box)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect((window_width / 2) - 288, (window_height / 2) - 200, 576, 200))  # size for scroll area
        self.scrollArea.setMaximumSize(QtCore.QSize(576, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 559, 136))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # Grid Layout
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

        try:
            if len(self.website_list) > 0:
                rows = 4
                for websiteToggle in self.website_list:
                    self.createSite(rows)
                    self.createCheckBoxButton(rows)
                    self.createDelButton(rows)
                    self.sites[self.siteIndex - 1].setPlainText(websiteToggle[0])
                    self.checkBox[self.cbIndex - 1].setChecked(websiteToggle[1].strip() == "True")
                    rows += 1
        
        except AttributeError:
            for i in range(4, 6):
                self.createSite(i)
                self.createCheckBoxButton(i)
                self.createDelButton(i)


        self.blockedLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blockedLabel.setStyleSheet("color:     #95bfe7")
        self.blockedLabel.setObjectName("blockedLabel")
        self.gridLayout.addWidget(self.blockedLabel, 2, 1, 1, 1)
        self.addNewButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.addNewButton.setStyleSheet("color:     #95bfe7")
        self.addNewButton.setObjectName("addNewButton")
        self.gridLayout.addWidget(self.addNewButton, 2, 2, 1, 1)
        self.blockedSitesLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blockedSitesLabel.setStyleSheet("color:     #95bfe7")
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
        self.saveButton.clicked.connect(self.file2)
        self.saveButton.clicked.connect(MainWindow.hide)
    
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
                                           "font-size:15pt; font-weight:400; font-style:normal;\">\n "
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

        # Deleted a row
        for button in self.deleteButton:
            if button.clicked:
                row = self.deleteButton.index(button)
                self.deleteButton[row].clicked.connect(self.deleteRow)

    # This function blocks the websites with inputed hour and min. Once the new hour and min duration is over, the funcion blocks the websites
    # hostsPath -> string
    # websiteList -> list
    # hour -> int
    # mins -> int
    def websiteBlocker(self, hostsPath, websiteList, hour, mins):
        """ This function blocks the websites with inputed hour
        and min. Once the new hour and min duration is over, the
        funcion blocks the websites

        Args:
            hostsPath(str): Directory to the hosts file
            websiteList(list): A list of blocked website url
            hour(int): How many hours are blocked
            mins(int): How many mins are blocked
        """
        # Redirect to hosts file
        redirect = "127.0.0.1"

        print('blocked')
        # Then redirect the blocked websites
        with open(hostsPath, 'r+') as hostsfile:
            host_content = hostsfile.read()
            for site in websiteList:
                if site not in host_content:
                    hostsfile.write(redirect + " " + site + "\n")

    
    def saveClicked(self):
        for i in range(len(self.sites)):
            link = str(self.sites[i].toPlainText())
            checked = self.checkBox[i].isChecked()
            if link != "":
                self.settingsList.append([link, checked])
        if self.hoursField.toPlainText().strip() != "" and self.minutesField.toPlainText().strip():
            #self.settingsList.append([self.hoursField.toPlainText().strip(), self.minutesField.toPlainText().strip()])
            self.hour = self.hoursField.toPlainText().strip()
            self.minute = self.minutesField.toPlainText().strip()
        
        elif self.hoursField.toPlainText().strip() != "" and self.minutesField.toPlainText().strip() == "":
            #self.settingsList.append([self.hoursField.toPlainText().strip(), "00"])
            self.minute = 0
            self.hour = self.hoursField.toPlainText().strip()
        
        elif self.hoursField.toPlainText().strip() == "" and self.minutesField.toPlainText().strip() != "":
            #self.settingsList.append(["0", self.minutesField.toPlainText().strip()])
            self.hour = 0
            self.minute = self.minutesField.toPlainText().strip()
    
        websites = []
        print(len(self.settingsList))
        for i in range(len(self.settingsList)):
            print('sett')
            print(self.settingsList[i])
            sites = self.settingsList[i]
            link = sites[0]
            websites.append(link)
            writeFile(self.settingsList, "data.csv")
        
        self.ui.setHour(int(self.hour))
        self.ui.setMinute(int(self.minute))
        self.websiteBlocker(settings.hostPath, websites, self.hour, self.minute)
        
        self.hour = self.hoursField.toPlainText().strip()
        self.minute = self.minutesField.toPlainText().strip()
    
    def getMinute(self):
        return self.minute

    def getHour(self):
        return self.hour
    
    def deleteRow(self, row):
        self.deleteButton[row].deleteLater()
        self.deleteButton.pop(0)
        self.gridLayout.itemAt(0).widget().deleteLater()
        self.gridLayout.itemAt(1).widget().deleteLater()
        self.gridLayout.itemAt(2).widget().deleteLater()

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
        self.sites[self.siteIndex].setStyleSheet("background-color: #c8daf2")
        self.sites[self.siteIndex].setObjectName("site" + str(self.siteNum))
        self.gridLayout.addWidget(self.sites[self.siteIndex], row, 0, 1, 1)
        self.siteNum += 1
        self.siteIndex += 1
        self.row += 1

    def createCheckBoxButton(self, row):
        self.checkBox.append(QtWidgets.QCheckBox(self.scrollAreaWidgetContents))
        self.checkBox[self.cbIndex].setText("")
        self.checkBox[self.cbIndex].setStyleSheet("background-color: #173364")
        self.checkBox[self.cbIndex].setObjectName("checkBox1")
        self.gridLayout.addWidget(self.checkBox[self.cbIndex], row, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.cbIndex += 1
        self.cbNum += 1

    def createDelButton(self, row):
        _translate = QtCore.QCoreApplication.translate
        self.deleteButton.append(QtWidgets.QPushButton(self.scrollAreaWidgetContents))
        self.deleteButton[self.dbIndex].setStyleSheet("background-color: #173364; color: #c8daf2")
        self.deleteButton[self.dbIndex].setObjectName("deleteButton" + str(self.dbNum))
        self.deleteButton[self.dbIndex].setText(_translate("MainWindow", "Delete"))
        self.gridLayout.addWidget(self.deleteButton[self.dbIndex], row, 2, 1, 1)
        self.dbIndex += 1
        self.dbNum += 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.connectActions()
    MainWindow.show()
    sys.exit(app.exec_())
