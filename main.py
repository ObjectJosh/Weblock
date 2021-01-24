from site_blocker import *
from adding_current_time import *

def make_website_list(load):
    websites = load[:-1]
    website_list = []
    for website in websites:
        website_list.append(website[0])
    return website_list

def get_hour(load):
    return load[-1][0]

def get_minute(load):
    return load[-1][1]

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.connectActions()
    MainWindow.show()
    if ui.saveNum == 1:
        load = readFile("siteNames.csv")
        website_list = make_website_list(load)
        hour = get_hour(load)
        minute = get_minute(load)
        websiteBlocker(r"C:\Windows\System32\drivers\etc", website_list, hour, minute)
    sys.exit(app.exec_())


