# The survey screen which shows the countdown timer and survey input fields user wishes to override the timer

from PyQt5 import QtCore, QtGui, QtWidgets
import block_sites_screen as screen_file
import time
import settings

class UIWindow(object):
    """ The Survey Screen window """
    def __init__(self):
        """ Initializes the UIWindow """
        self.count = 0
        self.start = False
        self.unblock = False
        self.timer = QtCore.QTimer()
        self.timer.start(1000) # updates the timer display every second
        self.time_list = []
        self.web_list = None
        self.override = False
        self.duration_hour = 0
        self.duration_minute = 0
    
    def setupUi(self, ShownWindow):
        """ Setup Elements in the SurveyWindow
        
        Args:
            ShownWindow(QMainWindow): the shown window, which is the survey window
        """
        # Window set up
        self.ShownWindow = ShownWindow
        ShownWindow.setObjectName("Web Blocker")
        ShownWindow.resize(settings.survey_window_size[0], settings.survey_window_size[1])
        window_width = int(self.ShownWindow.frameGeometry().width())
        window_height = int(self.ShownWindow.frameGeometry().height())
        ShownWindow.setStyleSheet("background-color: #1961b2")

        # Central Widget -> Widget
        self.centralwidget = QtWidgets.QWidget(ShownWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Survey Question Layout (change this to move all survey questions)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect((window_width / 2) - 210, (window_height / 2) - 150, 420, 343))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Survey Question 1 Label -> Label
        self.q1label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.q1label.setStyleSheet("color:     #95bfe7; background-color: #173364")
        self.q1label.setObjectName("q1label")
        self.verticalLayout.addWidget(self.q1label)
        
        # Survey Question 1 Input Field -> TextEdit
        self.q1input = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.q1input.setStyleSheet("background-color: #c8daf2")
        self.q1input.setObjectName("q1input")
        self.verticalLayout.addWidget(self.q1input)
        
        # Survey Question 2 Label -> Label
        self.q2label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.q2label.setStyleSheet("color:     #95bfe7; background-color: #173364")
        self.q2label.setObjectName("q2label")
        self.verticalLayout.addWidget(self.q2label)
        
        # Survey Question 2 Input Field -> TextEdit
        self.q2input = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.q2input.setStyleSheet("background-color: #c8daf2")
        self.q2input.setObjectName("q2input")
        self.verticalLayout.addWidget(self.q2input)
        
        # Survey Question 3 Label -> Label
        self.q3label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.q3label.setStyleSheet("color:     #95bfe7; background-color: #173364")
        self.q3label.setObjectName("q3label")
        self.verticalLayout.addWidget(self.q3label)
        
        # Survey Question 3 Input Field -> TextEdit
        self.q3input = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.q3input.setStyleSheet("background-color: #c8daf2")
        self.q3input.setObjectName("q3input")
        self.verticalLayout.addWidget(self.q3input)
        
        # Confirmation Checkbox -> CheckBox
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setStyleSheet("color:     #95bfe7")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        
        # Comfirm Button (change this to move the Confirm Button) -> Button
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect((window_width / 2) - 60, (window_height / 2) + 220, 120, 32))
        self.confirmButton.setStyleSheet("color:     #c8daf2; background-color: #173364")
        self.confirmButton.setObjectName("confirmButton")
        
        # Time Dialog LCD Display (change this to move the Time Dialog) -> LCDNumber
        self.timeDialog = QtWidgets.QLCDNumber(self.centralwidget)
        self.timeDialog.setGeometry(QtCore.QRect((window_width / 2) - 95, (window_height / 2) - 230, 190, 60))
        self.timeDialog.setMinimumSize(QtCore.QSize(190, 60))
        self.timeDialog.setStyleSheet("background-color:    #c8daf2; color:     #173364")
        self.timeDialog.display("00:00") # set initial time dialog to display "00:00"
        self.timeDialog.setObjectName("timeDialog")
        
        # Time Remaining Label (change this to move the "Time Remaining" Label) -. Remaining Time
        self.timeRemaining = QtWidgets.QLabel(self.centralwidget)
        self.timeRemaining.setGeometry(QtCore.QRect((window_width / 2) - 70, (window_height / 2) - 270, 140, 30))
        self.timeRemaining.setFont(QtGui.QFont("Arial", 18))
        self.timeRemaining.setStyleSheet("color: #c8daf2")
        self.timeRemaining.setObjectName("timeRemaining")
        ShownWindow.setCentralWidget(self.centralwidget)
        
        # Menu Bar -> MenuBar
        self.menubar = QtWidgets.QMenuBar(ShownWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 22))
        self.menubar.setObjectName("menubar")
        ShownWindow.setMenuBar(self.menubar)
        self.retranslateUi(ShownWindow)
        QtCore.QMetaObject.connectSlotsByName(ShownWindow)

    def retranslateUi(self, ShownWindow):
        """ Writes the message into the textbox of surveyScreen Window 
        
        Args:
            ShownWindow(QMainWindow): The Window that is currently shown.
        """
        _translate = QtCore.QCoreApplication.translate
        ShownWindow.setWindowTitle(_translate("Web Blocker", "Web Blocker"))
        self.q1label.setText(_translate("Web Blocker", "   Why would you like to stop blocking?"))
        self.q2label.setText(_translate("Web Blocker", "   What are you currently working on right now?"))
        self.q3label.setText(_translate("Web Blocker", "   What do you still need to get done?"))
        self.checkBox.setText(_translate("Web Blocker", "  I hereby agree that I am unblocking these sites for a good reason"))
        self.confirmButton.setText(_translate("Web Blocker", "Confirm"))
        self.timeRemaining.setText(_translate("Web Blocker", "Time Remaining"))

    def connectActions(self, SurveyWindow):
        """ Connect click events in the SurveyWindow """
        self.timer.timeout.connect(self.update_time)
        self.startTimer()
        self.duration_seconds = 1
        self.confirmButton.clicked.connect(self.confirm_clicked)
    
    def update_time(self):
        """ Updates the count_down of given time """
        self.web_list = self.now_get_sites()
        self.countdown()

    def now_get_sites(self):
        """ Creates a list of websites as strings and returns it
        
        Returns:
            site_lists(list): list of websites as strings
        """
        self.time_list = screen_file.readFile("data.csv")
        site_lists = []
        site_lists.append(self.time_list[0])
        for i in self.time_list[1:]:
            site_lists.append(i[0])
        return site_lists
    
    def close_blocker(self, website_list):
        """ This function clears the websites written in the 'hosts' file

        Args:
            website_list(list): list of blocked websites as strings
        """
        try:
            with open(settings.hostPath, 'r+') as hostsfile:
                content = hostsfile.readlines()
                hostsfile.seek(1)
                for line in content:
                    if not any(site in line for site in website_list):
                        hostsfile.write(line)
                    hostsfile.truncate()
        except FileNotFoundError:
            print("Error: hosts file not found")
    
    def confirm_clicked(self):
        """ When 'Confirm' is clicked, check that all fields have text and confirmation checkbox is checked """
        q1Text = self.q1input.toPlainText().strip()
        q2Text = self.q2input.toPlainText().strip()
        q3Text = self.q3input.toPlainText().strip()
        checkBoxChecked = self.checkBox.isChecked()
        # All fields are filled
        if q1Text != "" and q2Text != "" and q3Text != "" and checkBoxChecked:
            self.q1input.setStyleSheet("background-color: #c8daf2")
            self.q2input.setStyleSheet("background-color: #c8daf2")
            self.q3input.setStyleSheet("background-color: #c8daf2")
            self.checkBox.setStyleSheet("color: #95bfe7")
            self.close_blocker(self.web_list[1:])
            self.override = True
            print("Override Complete: Sites are now unblocked")
        # Fields are still blank
        else:
            if q1Text == "":
                self.q1input.setStyleSheet("background-color: #ffb3b3")
            if q2Text == "":
                self.q2input.setStyleSheet("background-color: #ffb3b3")
            if q3Text == "":
                self.q3input.setStyleSheet("background-color: #ffb3b3")
            if not checkBoxChecked:
                self.checkBox.setStyleSheet("color: #ffb3b3")
            print("Override Incomplete")
    
    def countdown(self):
        """ Countdown timer of given time, and formats to hour/minute 
        if hour != 0 and formats minute/seconds if hour == 0 """
        if self.start == True:
            self.duration_seconds -= 1
            
            # Check if confirm override is clicked
            if self.override == True:
                self.duration_minute = 0
                self.duration_hour = 0
                self.duration_seconds = 0
                self.start = 0
           
            # Check if timer is done
            if self.duration_hour == 0 and self.duration_minute == 0 and self.duration_seconds == 0:
                self.duration_minute = 0
                self.start = False
                self.close_blocker(self.web_list[1:])
                print("Timer done")

            # Resets seconds after its done 
            elif self.duration_seconds == 0:
                self.duration_seconds = 59
                self.duration_minute -= 1
            
            # Resets minutes after its done
            if self.duration_minute == -1 and self.duration_hour != 0:
                self.duration_minute = 59
                self.duration_hour -= 1
            
            # Format the time
            timeformatHourMin = '{:02d}:{:02d}'.format(self.duration_hour, self.duration_minute)
            timeformatMinSec = '{:02d}:{:02d}'.format(self.duration_minute, self.duration_seconds)
            
            # Format depending if hour/min or min/sec
            if self.duration_hour != 0:
                self.timeDialog.display(timeformatHourMin)
            elif self.duration_hour == 0:
                self.timeDialog.display(timeformatMinSec)

    def startTimer(self):
        """ Starts the countdown timer """
        self.start = True
        if self.count == 0:
            self.start == False
    
    def setMinute(self, dur_min):
        """ Update the amount of minutes in the UIWindow

        Args:
            dur_min(int): the number of minutes being blocked
        """
        self.duration_minute = dur_min

    def setHour(self, dur_hour):
        """ Updates the amount of hours in the UIWindow
        
        Args:
            dur_hour(int): the number of hours being blocked
        """
        self.duration_hour = dur_hour
