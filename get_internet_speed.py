import subprocess
import admin
from admin import checkPrivilege

def netstat_e():
    # checkPrivilege()
    x = subprocess.Popen("netstat -e",stdout=subprocess.PIPE)
    text = x.stdout.read()
    # print text[79:132],
    # print text.split()
    return text.split()
def getTotalNetUsage():
    x = netstat_e()
    recvBytes = int(x[5])
    sentBytes = int(x[6])
    totalBytes = int(recvBytes)+int(sentBytes)
    return recvBytes, sentBytes, totalBytes
