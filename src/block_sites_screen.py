# The initial screen for setting the sites which the user would like to block

from PyQt5 import QtCore, QtGui, QtWidgets
from survey_screen import UIWindow, MySurveyWindow
import sys
import settings
from functools import partial

class Ui_MainWindow(object):
    """ The Block Site window """

    def __init__(self):
        """ Initializes the Ui_MainWindow """
        self.MainWindow = None
        self.surveyWindow = UIWindow()
        # Starting row
        self.row = 1

        # Site
        self.sites = []

        # Delete Button
        self.deleteButton = []

        # Checkbox
        self.checkBox = []

        # Time
        self.hour = 0
        self.minute = 0

        # Website List
        self.website_list = []

        # List From Data
        temp_list = readFile("data.csv")
        try:
            int(temp_list[-1][0])
            self.website_list = temp_list[:-1]
        except IndexError: 
            self.website_list = []
        except ValueError:
            self.website_list = temp_list

        # Settings List
        self.settingsList = []

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox()
        close.setText("You sure?")
        close.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        close = close.exec()

        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def switch_screens(self):
        """ Switches the screens from MainWindow to SurveyWindow """
        self.shownWindow = MySurveyWindow()
        self.shownWindow.passWindowObject(self.surveyWindow)
        self.surveyWindow.setupUi(self.shownWindow)
        self.surveyWindow.connectActions(self.shownWindow)
        self.surveyWindow.setHour(int(self.surveyWindow.duration_hour))
        self.surveyWindow.setMinute(int(self.surveyWindow.duration_minute))
        self.shownWindow.show()

    def setupUi(self, MainWindow):
        """ Setup Elements in the MainWindow

        Args:
            MainWindow(QMainWindow): the main window
        """
        # Window set up
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(settings.block_window_size[0], settings.block_window_size[1])
        window_width = int(self.MainWindow.frameGeometry().width())
        window_height = int(self.MainWindow.frameGeometry().height())
        self.MainWindow.setStyleSheet("background-color: #1961b2\n")

        # Central Widget -> Widget
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Set Duration Label (change this to move "Set Duration" label) -> Widget
        self.setDurationLabel = QtWidgets.QLabel(self.centralwidget)
        self.setDurationLabel.setGeometry(QtCore.QRect((window_width / 2) - 70, (window_height / 2) + 50, 140, 30))
        self.setDurationLabel.setStyleSheet("color: #95bfe7")
        self.setDurationLabel.setObjectName("setDurationLabel")

        # Grid Layout for Sites (change this to move hour/minute text fields) -> Widget
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect((window_width / 2) - 133, (window_height / 2) + 50, 266, 64))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        # Grid Layout for Duration -> GridLayout
        self.durationGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.durationGridLayout.setContentsMargins(0, 0, 0, 0)
        self.durationGridLayout.setObjectName("durationGridLayout")

        # Minutes Text Field -> TextEdit
        self.minutesField = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.minutesField.setMaximumSize(QtCore.QSize(150, 30))
        self.minutesField.setStyleSheet("background-color: #c8daf2")
        self.minutesField.setObjectName("minutesField")
        self.durationGridLayout.addWidget(self.minutesField, 1, 1, 1, 1)

        # Minutes Label -> Label
        self.minutesLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.minutesLabel.setStyleSheet("color: #95bfe7")
        self.minutesLabel.setObjectName("minutesLabel")
        self.durationGridLayout.addWidget(self.minutesLabel, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)

        # Hours Text Field -> TextEdit
        self.hoursField = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.hoursField.setMaximumSize(QtCore.QSize(150, 25))
        self.hoursField.setStyleSheet("background-color: #c8daf2")
        self.hoursField.setObjectName("hoursField")
        self.durationGridLayout.addWidget(self.hoursField, 1, 0, 1, 1)

        # Hours Label -> Label
        self.hoursLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.hoursLabel.setStyleSheet("color:     #95bfe7")
        self.hoursLabel.setObjectName("hoursLabel")
        self.durationGridLayout.addWidget(self.hoursLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)

        # Title Label: "Web Blocker" -> Label
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect((window_width / 2) - 120, (window_height / 2) - 270, 240, 50))
        self.titleLabel.setStyleSheet("color:     #95bfe7")
        self.titleLabel.setObjectName("titleLabel")

        # Save Button (change this to move the Save button) -> Button
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect((window_width / 2) - 55, (window_height / 2) + 140, 110, 31))
        self.saveButton.setStyleSheet("background-color: #173364; color:     #c8daf2")
        self.saveButton.setObjectName("saveButton")

        # Scroll Area for Sites (change this to move sites box) -> ScrollArea
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect((window_width / 2) - 288, (window_height / 2) - 200, 576, 200))  # size for scroll area
        self.scrollArea.setMaximumSize(QtCore.QSize(576, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 559, 136))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # Grid Layout -> GridLayout
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

        # Block Sites -> Label
        self.blockedSitesLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blockedSitesLabel.setStyleSheet("color:     #95bfe7")
        self.blockedSitesLabel.setObjectName("blockedSitesLabel")
        self.gridLayout.addWidget(self.blockedSitesLabel, self.row, 0, 1, 1) 

        # scrollArea -> ScrollArea
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.MainWindow.setCentralWidget(self.centralwidget)

        # Blocked -> Label
        self.blockedLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blockedLabel.setStyleSheet("color:     #95bfe7")
        self.blockedLabel.setObjectName("blockedLabel")
        self.gridLayout.addWidget(self.blockedLabel, self.row, 1, 1, 1)

        # Add New -> Button
        self.addNewButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.addNewButton.setStyleSheet("color:     #95bfe7")
        self.addNewButton.setObjectName("addNewButton")
        self.gridLayout.addWidget(self.addNewButton, self.row, 2, 1, 1)
        self.row += 1

        # Creates a check and delete button for every row
        try:
            if len(self.website_list) > 0:
                for websiteToggle in self.website_list[1:]:
                    self.newRow()
                    self.sites[-1].setPlainText(websiteToggle[0])
                    self.checkBox[-1].setChecked(websiteToggle[1].strip() == "True")
        # If there is no starting data, make 3 blank rows
        except AttributeError:
            for _ in range(3):
                self.newRow()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """ Formats elements in the MainWindow

        Args:
            MainWindow(QMainWindow): the main window
        """
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        """ Connect click events in the MainWindow """
        # Save Button is Clicked
        self.saveButton.clicked.connect(self.saveClicked)
        #self.saveButton.clicked.connect(self.MainWindow.hide)

        # Add New Row is Clicked
        self.addNewButton.clicked.connect(self.newRow)

        # Delete Row is Clicked
        self.connectButtons()

    def disconnectButtons(self):
        """ Disonnect click events for 'Delete' buttons in the MainWindow. Acts as a reset to current connections """
        for i in range(len(self.deleteButton)):
            self.deleteButton[i].clicked.disconnect()

    def connectButtons(self):
        """ Connect click events for 'Delete' buttons in the MainWindow """
        for i in range(len(self.deleteButton)):
            self.deleteButton[i].clicked.connect(partial(self.deleteRow, i))

    def websiteBlocker(self, hostsPath, websiteList):
        """ This function blocks the websites with inputed hour
        and min. Once the new hour and min duration is over, the
        funcion blocks the websites

        Args:
            hostsPath(str): Directory to the hosts file
            websiteList(list): A list of blocked website url
        """
        # Redirect port
        redirect = "127.0.0.1"

        # Redirect the blocked websites
        try:
            with open(hostsPath, 'r+') as hostsfile:
                host_content = hostsfile.read()
                for site in websiteList:
                    if site not in host_content:
                        hostsfile.write(redirect + " " + site + "\n")
            print("Successfully Blocked")
        except FileNotFoundError:
            print("Error: hosts file not found")

    def saveClicked(self):
        """ Whenever save button is clicked, it reads text from the text box and stores them
        into 'data.csv' for use in the survey window. Then checks if it should switch screens. """
        hoursFieldText = self.hoursField.toPlainText().strip()
        minutesFieldText = self.minutesField.toPlainText().strip()
        # If both 'Hours' text field and 'Minutes' text field are filled
        if hoursFieldText != "" and minutesFieldText != "":
            self.hour = hoursFieldText
            self.minute = minutesFieldText
        # If only 'Hours' text field is filled
        elif hoursFieldText != "" and minutesFieldText == "":
            self.minute = 0
            self.hour = hoursFieldText
        # If only 'Minutes' text field is filled
        elif hoursFieldText == "" and minutesFieldText != "":
            self.hour = 0
            self.minute = minutesFieldText

        # Update current websites & settings list
        self.update_settingsList()

        # Update survey window's countdown time
        self.surveyWindow.setHour(int(self.hour))
        self.surveyWindow.setMinute(int(self.minute))

        # Write data into file
        writeFile(self.settingsList, "data.csv")

        # If timer is filled
        if self.hour != 0 or self.minute != 0:
            # Start blocking
            self.websiteBlocker(settings.hostPath, self.site_list())
            # Switch screens
            self.MainWindow.hide()
            self.switch_screens()
        self.settingsList = []

    def update_settingsList(self):
        """ Updates the settingList, with time and non-empty sites """
        self.settingsList.append([self.hour, self.minute])
        # Checking if sites-box is not empty
        for i in range(len(self.sites)):
            link = str(self.sites[i].toPlainText())
            checked = self.checkBox[i].isChecked()
            if link != "":
                self.settingsList.append([link, checked])

    def site_list(self):
        """ Creates a list of websites as strings, which will be blocked

        Returns:
            websites(list): list of websites as strings, to be blocked
        """
        websites = []
        for i in range(1, len(self.settingsList)):
            sites = self.settingsList[i]
            if sites[1]:
                link = sites[0]
                websites.append(link)
        return websites

    def deleteRow(self, button_list_idx):
        """ This function deletes a single row from the MainWindow

        Args:
            button_list_idx(int): the index of the button which was clicked in deleteButton list
        """
        grid_index = (button_list_idx + 1) * 3
        self.gridLayout.itemAt(grid_index).widget().deleteLater()
        self.gridLayout.itemAt((grid_index) + 1).widget().deleteLater()
        self.gridLayout.itemAt((grid_index) + 2).widget().deleteLater()
        self.disconnectButtons()
        self.deleteButton.pop(button_list_idx)
        self.sites.pop(button_list_idx)
        self.checkBox.pop(button_list_idx)
        self.connectButtons()

    def newRow(self):
        """ This function adds a single new row to the MainWindow """
        # Create Site
        self.createSite()
        # Create CheckBox
        self.createCheckBoxButton()
        # Create Delete Button
        self.createDelButton()

        self.row += 1
        self.connectButtons()

    def createSite(self):
        """ This function creates a new-site(text-box) to MainWindow """
        self.sites.append(QtWidgets.QTextEdit(self.scrollAreaWidgetContents))
        self.sites[-1].setMinimumSize(QtCore.QSize(351, 31))
        self.sites[-1].setMaximumSize(QtCore.QSize(351, 31))
        self.sites[-1].setStyleSheet("background-color: #c8daf2")
        self.sites[-1].setObjectName("site" + str(len(self.sites)))
        self.gridLayout.addWidget(self.sites[-1], self.row, 0, 1, 1)

    def createCheckBoxButton(self):
        """ This function creates a new CheckBox to the MainWindow """
        self.checkBox.append(QtWidgets.QCheckBox(self.scrollAreaWidgetContents))
        self.checkBox[-1].setText("")
        self.checkBox[-1].setStyleSheet("background-color: #173364")
        self.checkBox[-1].setObjectName("checkBox1")
        self.gridLayout.addWidget(self.checkBox[-1], self.row, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.checkBox[-1].setChecked(True)

    def createDelButton(self):
        """ This function creates a new Delete-Button to the MainWindow """
        _translate = QtCore.QCoreApplication.translate
        self.deleteButton.append(QtWidgets.QPushButton(self.scrollAreaWidgetContents))
        self.deleteButton[-1].setStyleSheet("background-color: #173364; color: #c8daf2")
        self.deleteButton[-1].setObjectName("deleteButton" + str(len(self.deleteButton)))
        self.deleteButton[-1].setText(_translate("MainWindow", "Delete"))
        self.gridLayout.addWidget(self.deleteButton[-1], self.row, 2, 1, 1)

class MyWindow(QtWidgets.QMainWindow):
    """ MyWindow implements QMainWindow, used for the close window listener """

    def closeEvent(self, event):
        """ Listens for close window event and sends confirmation message box

        Args:
            event(event): the event call
        """
        result = QtWidgets.QMessageBox.question(self, "Confirm Exit...", "Are you sure you want to exit?", QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        event.ignore()
        if result == QtWidgets.QMessageBox.Yes:
            event.accept()

def readFile(fileName):
    """ This function reads the contents of the data.csv file

    Arguments:
        fileName(string): the name of the data file
    Returns:
        websites(list): the list of websites of format ['url'(str),'if checked'(str)]
    """
    websites = []
    try:
        websites_file = open(fileName, "r")
        for line in websites_file:
            line = line.split(",")
            settings = [line[0], line[1]]
            websites.append(settings)
        websites_file.close()
    # If the file is not found, that means there is no saved data yet
    except FileNotFoundError:
        pass
    return websites

def writeFile(settings, fileName):
    """ This function writes the contents into the data.csv file 

    Arguments:
        settings(list): list of each site's data and settings
        fileName(string): the name of the data file
    """
    output = open(fileName, "w")
    for setting in settings:
        output.write(str(setting[0]) + "," + str(setting[1]) + "\n")
    output.close()
    print("Successfully Saved")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    surveyWindow = Ui_MainWindow()
    surveyWindow.setupUi(MainWindow)
    surveyWindow.connectActions()
    MainWindow.show()
    sys.exit(app.exec_())
