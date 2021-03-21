import block_sites_screen as screen_file
from PyQt5 import QtWidgets
import sys
import settings
import platform

if __name__ == "__main__":
    block_size_tuple = (800, 630)
    survey_size_tuple = (780, 600)
    hostPath = ""
    if platform.system() == "Darwin":
        hostPath = r"/private/etc/hosts"
    elif platform.system() == "Windows":
        hostPath = r"C:\Windows\System32\drivers\etc\hosts"
    else:
        print("Your system is unsupported. This application supports OS and Windows.")
        exit()
    settings.init(hostPath, block_size_tuple, survey_size_tuple)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = screen_file.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.connectActions()
    MainWindow.show()
    sys.exit(app.exec_())
