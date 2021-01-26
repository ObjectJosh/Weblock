from site_blocker import *

# def get_ui():
#     return ui

# def init():
#     global ui
#     ui = Ui_MainWindow()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.connectActions()
    MainWindow.show()
    sys.exit(app.exec_())
