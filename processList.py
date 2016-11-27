import subprocess
import admin, sys
from admin import checkPrivilege
from collections import defaultdict
import re

def netstat_b_o():
    #print "\n*****************************************************************************************"
    checkPrivilege()
    # subprocess.call("netstat -b -o")
    try:
        x = "kooko"
        print x
        x = subprocess.Popen("netstat -b -o",stdout=subprocess.PIPE)
        # print x.stdout.read()
        text = x.stdout.read()
    # x = subprocess.check_output("cmd -command \"netstat -e -o\"")
    except:
        print "============>>> ",x
    # print "+++++++++++++++",x," .. ",text
    return text

def TCP_List():
    x=netstat_b_o()
    print x
    grp = re.findall(r'\[([a-zA-Z.]*)\]',x)
    print  grp
    exe = list()
    for i in grp:
        exe.append(i)
        # print i," --> ",
    # print '\n',exe
    return exe

def ProcessTable(Plist):
    d = dict()
    for element in Plist:
		if element in d:
			# increments the number in the list
			d[element][0] += 1
		else:
			# creates a new list
			d[element] = []
			d[element].append(1)
    # sorted(d, key = lambda k: k[0])
    return d

def getProcessTable():
    tex = TCP_List()
    return ProcessTable(tex)
