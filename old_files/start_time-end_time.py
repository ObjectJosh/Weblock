# Import libraries
import time
import datetime

def time_differ(nowTime, endTime):
    """ This function calculates the time difference one one time to another
    and returns the minute difference
    
    Args:
        nowTime(int): The earlier time
        endTime(int): The later time
    
    Returns:
         time(int): Return the minute difference
    """
    timeA = datetime.datetime.strptime(endTime, "%H:%M")
    timeB = datetime.datetime.strptime(nowTime, "%H:%M")
    newTime = timeA - timeB
    return newTime.seconds/60

def largest_divisible(number):
    """ This function finds the largest divisible number for an int
    between 0 - 200, and returns the largest divisible. 

    Args:
        number(int): Any int
    
    Returns:
        int(int): Returns the largest divisible between 0 -200
    """
    maxed = 200
    i = 0
    n = maxed
    while i < maxed:
        if number % n == 0:
            i = maxed
            return n
        n -= 1

def close_blocker():
    """ This function instantly deletes the website blocker and 
    stops the program
    """
    with open(hostsPath, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(site in line for site in websiteList):
                file.write(line)
            file.truncate()
    running = False
    return running

def countdown_time(times, wait):
    """ This functions holds the program until
    it hits the correct time.

    Args:
        times(int): Time difference between to times
        wait(int): How long the function waits per interval
    """
    i = 0
    while i < times:
        i += wait
        time.sleep(wait * 60)

# websiteList -> list
# earlyTime -> int
# lateTime -> int
# hostsPath -> string (taken from bash file so that we can use it for both Mac and Windows OS)

def websiteBlocker(hostsPath, websiteList, earlyTime, lateTime):
    """ This function blocks websites during earlyTime
    and lateTime. Once duration is over it unblocks the
    websites
    
    Args:
        hostsPath(str): Directory to the host file
        websiteList(list): A list of blocked website url
        earlyTime(str): Start time in 24 hour format
        lateTime(str): End time in 24 hour format
    """
    # Redirect to host file
    redirect = "127.0.0.1"
    
    beginTime = time.strftime('%H:%M:%S')[:5]

    # Website blocker will block if you're within the specified period of time 
    if beginTime > earlyTime:
        print("Sorry Not Allowed...")
    else:
        print("Allowed access!")
    
    # Waits until current time == start time
    if beginTime < earlyTime:
        timer = time_differ(beginTime, earlyTime)
        sleep = largest_divisible(timer)
        countdown_time(timer, sleep)
    
    # Blocks the websites
    print('blocked')
    with open(hostsPath, 'r+') as hostsfile:
        host_content = hostsfile.read()
        for site in websiteList:
            if site not in host_content:
                hostsfile.write(redirect + " " + site + "\n")
    
    # Wait until current time == end time
    times = time_differ(earlyTime, lateTime)
    sleeper = largest_divisible(times)
    countdown_time(times, sleeper)
    
    # Unblocks the websites
    close_blocker()
    print('unblocked')
    
if __name__ == '__main__':
    websiteList = ["www.facebook.com"]
    hostsPath = "C:\Windows\System32\drivers\etc\hosts"
    websiteBlocker(hostsPath, websiteList, '16:55', '16:56')