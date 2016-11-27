import subprocess, re
import admin, get_process_path, get_internet_speed
from admin import checkPrivilege
from processList import getProcessTable
from get_internet_speed import getTotalNetUsage
from get_process_path import getProcessPathByPID, getProcessPathByName


checkPrivilege()
def AddRule( process, address):
    checkPrivilege()
    print subprocess.check_call("netsh advfirewall firewall add rule name=\"Block"+process+"\" dir=out action=block program=\""+address+"\"  enable=yes")
def Block(process):
    # checkPrivilege()
    print "==========================>>>>",process
    checkPrivilege()
    try:
        x = subprocess.call("netsh advfirewall firewall set rule name=\"Block"+process+"\" new enable=yes")
        print x
        if x==1:
            print "Adding new rule: -------->",process
            AddRule(process,getProcessPathByName(process))
            Block(process)
    except:
        ad = getProcessPathByName(process)
        print '--->',ad
        AddRule(process,ad)
        Block(process)
def Unblock(process):
    print 321
    print subprocess.call("netsh advfirewall firewall set rule name=\"Block"+process+"\" new enable=no")

# try:
# Block("Chrome")
# Unblock("Chrome")
# getProcessPathByPID("9168")
# except:
#     None

r,s,t =getTotalNetUsage()
print r,s,t
# pTable = getProcessTable()
# for i in pTable:
#     print i[:-4],
#     ad = getProcessPathByName(i[:-4])
#     print '--->',ad
#     pTable[i].append(ad)
# # AddRule(i,ad)
# # Block(i)
# # Unblock(i)
# print '\n'
# for i in pTable:
#     print i,pTable[i]


# getProcessPathByName('firefox')
# getProcessPathByPID("9168")
# print subprocess.check_output("powershell.exe")
# print subprocess.check_output("Get-Process -Id 6264 | Select-Object path")
# print subprocess.check_output("exit")
#subprocess.call('notepad')
