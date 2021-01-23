# Import libraries
import time
from datetime import datetime as dt


# websiteList -> list
# earlyTime -> int
# lateTime -> int
# hostsPath -> string (taken from bash file so that we can use it for both Mac and Windows OS)
def websiteBlocker(hostsPath, websiteList, earlyTime, lateTime):
    redirect = "127.0.0.1"

    # Add the website you want to block, only blocks from an hour to an hour so 9-5 but can't do 9:30 - 5:30 rn
    beginTime = dt.now().year, dt.now().month, dt.now().day, earlyTime
    nowTime = dt.now().year, dt.now().month, dt.now().day, dt.now().hour
    endTime = dt.now().year, dt.now().month, dt.now().day, lateTime

    # Website blocker will block if you're within the specified period of time
    if beginTime < nowTime < endTime:
        print("Sorry Not Allowed...")
    else:
        print("Allowed access!")
    while True:
        if beginTime < nowTime < endTime:
            with open(hostsPath, 'r+') as file:
                content = file.read()
                for site in websiteList:
                    if site in content:
                        pass
                    else:
                        file.write(redirect + " " + site + "\n")
        else:
            with open(hostsPath, 'r+') as file:
                content = file.readlines()
                file.seek(0)
            for line in content:
                if not any(site in line for site in websiteList):
                    file.write(line)
                file.truncate()
    time.sleep(5)


if __name__ == '__main__':
    beginTime = dt.now().year, dt.now().month, dt.now().day, 9
    nowTime = dt.now().year, dt.now().month, dt.now().day, dt.now().hour
    lateTime = dt.now().year, dt.now().month, dt.now().day, 17
    print(beginTime < nowTime < lateTime)
    websiteList = ["www.facebook.com/"]
    hostsPath = "C:\Windows\System32\drivers\etc\hosts"
    websiteBlocker(hostsPath, websiteList, 9, 17)
