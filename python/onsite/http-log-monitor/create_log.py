import sys, random, time, os
from math import floor

#Check http://www.w3.org/Daemon/User/Config/Logging.html for spec
template = '%s %s %s [%s] "%s" %s %s\n'

status=["200","303","400","404","500"]
methods=["GET", "DELETE", "PUT", "POST"]
paths=["/pages","/pages/create", "/pages/id", "/users/profile","/users/signout","/api/sync", "/api/stats"]

def createRemoteHost():
    return "192.168.1.1"

def createRemoteLogName():
    return "-"

def createUserName():
    return "-"

def createDate():
    now=time.gmtime()
    nbHours=floor((time.mktime(time.localtime())-time.mktime(time.gmtime()))/3600)
    sign="+" if nbHours>=0 else "-"
    value="0"+str(nbHours) if nbHours<10 else str(nbHours)
    return time.strftime("%d/%m/%Y:%H:%M:%S ",now)+sign+value+"00"

def createRequest():
    return " ".join([random.choice(methods), random.choice(paths)])

def createStatus():
    return random.choice(status)

def createBytes():
    return random.randrange(1000,10000,1)

def entry(content):
    return template % content

def main():
    """
    Given the template and above functions, keep adding entry to logs at random pace
    """
    pass


if __name__ == '__main__':
    sys.exit(main())
