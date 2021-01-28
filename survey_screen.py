from PyQt5 import QtCore, QtGui, QtWidgets
import block_sites_screen as screen_file
import time
import settings

class UIWindow(object):
    def __init__(self):
        self.count = 0
        self.start = False
        self.unblock = False
        self.timer = QtCore.QTimer()
        self.timer.start(1000) # updates the timer display every second
        self.time_list = []
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Web Blocker")
        MainWindow.resize(783, 600)
        MainWindow.setStyleSheet("background-color: #1961b2")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 120, 420, 343))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.q1label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.q1label.setStyleSheet("color:     #95bfe7; background-color: #173364")
        self.q1label.setObjectName("q1label")
        self.verticalLayout.addWidget(self.q1label)
        self.q1input = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.q1input.setStyleSheet("background-color: #c8daf2")
        self.q1input.setObjectName("q1input")
        self.verticalLayout.addWidget(self.q1input)
        self.q2label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.q2label.setStyleSheet("color:     #95bfe7; background-color: #173364")
        self.q2label.setObjectName("q2label")
        self.verticalLayout.addWidget(self.q2label)
        self.q2input = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.q2input.setStyleSheet("background-color: #c8daf2")
        self.q2input.setObjectName("q2input")
        self.verticalLayout.addWidget(self.q2input)
        self.q3label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.q3label.setStyleSheet("color:     #95bfe7; background-color: #173364")
        self.q3label.setObjectName("q3label")
        self.verticalLayout.addWidget(self.q3label)
        self.q3input = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.q3input.setStyleSheet("background-color: #c8daf2")
        self.q3input.setObjectName("q3input")
        self.verticalLayout.addWidget(self.q3input)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setStyleSheet("color:     #95bfe7")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(310, 490, 121, 32))
        self.confirmButton.setStyleSheet("color:     #c8daf2; background-color: #173364")
        self.confirmButton.setObjectName("confirmButton")
        self.timeDialog = QtWidgets.QLCDNumber(self.centralwidget)
        self.timeDialog.setGeometry(QtCore.QRect(270, 50, 191, 61))
        self.timeDialog.setMinimumSize(QtCore.QSize(191, 61))
        self.timeDialog.setStyleSheet("background-color:    #c8daf2; color:     #173364")
        self.timeDialog.setObjectName("timeDialog")
        self.timeRemaining = QtWidgets.QLabel(self.centralwidget)
        self.timeRemaining.setGeometry(QtCore.QRect(305, 26, 140, 20))
        self.timeRemaining.setFont(QtGui.QFont("Arial", 18))
        self.timeRemaining.setStyleSheet("color:     #c8daf2")
        self.timeRemaining.setObjectName("timeRemaining")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Web Blocker", "Web Blocker"))
        self.q1label.setText(_translate("Web Blocker", "Why would you like to stop blocking?"))
        self.q2label.setText(_translate("Web Blocker", "What are you currently working on right now?"))
        self.q3label.setText(_translate("Web Blocker", "What do you still need to get done?"))
        self.checkBox.setText(_translate("MainWindow", "I hereby agree that I am unblocking these sites for a good reason "))
        self.confirmButton.setText(_translate("Web Blocker", "Confirm"))
        self.timeRemaining.setText(_translate("Web Blocker", "Time Remaining"))

    def connectActions(self, MainWindow):
        self.timer.timeout.connect(self.countdown)
        self.startTimer()
        self.seconds = 1

    def get_sites(self):
        self.time_list = screen_file.readFile("data.csv")
        site_lists = []
        for i in self.time_list: 
            site_lists.append(i[0])
        return site_lists
    
    def close_blocker(self, website_list):
        """ This function instantly deletes the website blocker and 
        stops the program
        """
        with open(settings.hostPath, 'r+') as file:
            content = file.readlines()
            file.seek(1)
            for line in content:
                if not any(site in line for site in website_list):
                    file.write(line)
                file.truncate()
        running = False
        return running
    
    def countdown(self):
        websites = self.get_sites()
        #print(websites)
        if self.start == True:
            self.seconds -= 1
            if self.hour == 0 and self.minute == 0 and self.seconds == 0:
                self.minute = 0
                self.start = False
                self.close_blocker(websites)
                print('Timer done')
            elif self.seconds == 0:
                self.seconds = 15
                self.minute -= 1
            if self.minute == -1 and self.hour != 0:
                print('h')
                self.minute = 59
                self.hour -= 1
            timeformatHourMin = '{:02d}:{:02d}'.format(self.hour, self.minute)
            timeformatMinSec = '{:02d}:{:02d}'.format(self.minute, self.seconds)
            if self.hour != 0 and self.seconds != 0:
                self.timeDialog.display(timeformatHourMin)
            if self.hour == 0:
                self.timeDialog.display(timeformatMinSec)
        
    def startTimer(self):
        self.start = True
        if self.count == 0:
            self.start == False
    
    def setMinute(self, min):
        self.minute = min

    def setHour(self, hour):
        self.hour = hour
