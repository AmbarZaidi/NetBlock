import subprocess

def getProcessPathByPID(Id):
    x = subprocess.check_output("powershell -command \"Get-Process -Id "+Id+" | Select-Object path\"")
    print "------------> ", x
    return x

def getProcessPathByName(process):
    x = subprocess.check_output("powershell -command \"Get-Process "+process+" | Select-Object path\"")
    # print "------------> ", x.split('\r\n')[3]#,x.split('\r\n')[3]
    return x.split('\r\n')[3]

# print subprocess.check_output("powershell -command \"Get-Process chrome | Select-Object path\"")
