import re

#     http://www.w3.org/Daemon/User/Config/Logging.html
#     remotehost rfc931 authuser [date] "request" status bytes
#     192.168.1.1 - - [08/04/2015:04:58:25 -0-5.000] "POST /pages/create" 303 2101
regex = '([(\d\.)]+) (.*?) (.*?) \[(.*?)\] "(.*?)" (\d+) (\d+)'

class LogEntry:

    def __init__(self, line):
       item = re.match(regex, line).groups()
       self.remotehost = item[0]
       self.rfc931 = item[1]
       self.authuser = item[2]
       self.date = item[3]
       self.request = item[4]
       self.status = item[5]
       self.bytes = item[6]

    def getRemotehost(self):
        return self.remotehost

    def getRfc931(self):
        return self.rfc931

    def getAuthuser(self):
        return self.authuser

    def getDate(self):
        return self.date

    def getRequest(self):
        return self.request

    def getRequestMethod(self):
        return self.request.split(" ")[0]

    def getRequestPath(self):
        return self.request.split(" ")[1]

    def getRequestSection(self):
        return self.request.split(" ")[1].split("/")[1]

    def getStatus(self):
        return self.status

    def getBytes(self):
        return self.bytes

    def isGoodRequest(self):
        return self.status[0] == '2'

    def isBadRequest(self):
        return self.status[0] == '4'

    def isServerError(self):
        return self.status[0] == '5'

