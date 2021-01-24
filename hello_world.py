from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class UIWindow(QMainWindow):
    def __init__(self):
        super(UIWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Web Blocker")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Label 1")
        self.label.move(50, 50)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Button 1")
        self.button1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you have clicked the button at least once")
        self.update()

    def update(self):
        self.label.adjustSize()
        print("button 1 was clicked")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UIWindow()

    win.show()
    sys.exit(app.exec_())

