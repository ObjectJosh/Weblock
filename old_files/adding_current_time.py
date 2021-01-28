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
def websiteBlocker(hostsPath, websiteList, hour, mins):
    """ This function blocks the websites with inputed hour
    and min. Once the new hour and min duration is over, the
    funcion blocks the websites

    Args:
        hostsPath(str): Directory to the host file
        websiteList(list): A list of blocked website url
        hour(int): How many hours are blocked
        mins(int): How many mins are blocked
    """
    # Redirect to host file
    redirect = "127.0.0.1"

    print('blocked')
    # Then redirect the blocked websites
    with open(hostsPath, 'r+') as hostsfile:
        host_content = hostsfile.read()
        for site in websiteList:
            if site not in host_content:
                hostsfile.write(redirect + " " + site + "\n")

if __name__ == '__main__':
    websiteList = ["m.mangabat.com", "mangabat.com"]
    hostsPath = "C:\Windows\System32\drivers\etc\hosts"
    websiteBlocker(hostsPath, websiteList, 0, 5)