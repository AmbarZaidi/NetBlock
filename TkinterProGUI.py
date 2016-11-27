# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt

import Tkinter as tk
import ttk

import time
import get_internet_speed
from get_internet_speed import getTotalNetUsage

import admin
from admin import checkPrivilege
import main
from main import Block, Unblock
import processList
from processList import getProcessTable
import get_process_path
from get_process_path import getProcessPathByPID, getProcessPathByName

# import urllib
# import json
#
# import pandas as pd
# import numpy as np

checkPrivilege()

LARGE_FONT= ("Verdana", 12)
SMALL_FONT = ("Verdana", 10)
style.use("ggplot")


f = Figure()
a = f.add_subplot(111)
f.set_figheight(240)

dList = []
uList = []
index = []

for i in range (1,100):
    index.append(i)
    dList.append(0.0)
    uList.append(0.0)

r,s,t = getTotalNetUsage()
last = [r,s,t]
time.sleep(0.5)
r,s,t = getTotalNetUsage()
cur = [r,s,t]
print "\tDown:\t\tUp"

def animate(i):
    global uList,dList,last,cur
    r,s,t = getTotalNetUsage()
    last[0] = cur[0]
    last[1] = cur[1]
    last[2] = cur[2]
    cur[0] = r
    cur[1] = s
    cur[2] = t
    dList.pop(0)
    uList.pop(0)

    print "\t",cur[0]-last[0],"\t\t",cur[1]-last[1]
    dList.append(abs(int(cur[0]-last[0])/10240.0/1.6))
    uList.append(abs(int(cur[1]-last[1])/10240.0/1.6))

    a.clear()
    a.plot( index, dList, "#00A3E0", label="UP")
    a.fill_between( index, dList)
    a.plot(index, uList,"#183A54" , label="DOWN") #"#F4C430"

    a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
             ncol=2, borderaxespad=0)
    title = "Current Net Usage\nD: "+str((cur[0]-last[0])/10240/1.6)+" kB/s        U: "+str((cur[1]-last[1])/10240/1.6)+" kB/s"
    a.set_title(title)


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Message")
    label = ttk.Label(popup, text=msg, font=SMALL_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


class NetControlApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "NetControl client")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command = lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        tk.Tk.config(self, menu=menubar)
        self.frames = {}

        # for F in ():

        for F in (StartPage, BTCe_Page, PageOne):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        frame = AppDetails(container, self)
        self.frames[AppDetails] = frame
        frame.grid(row=0, column=0, sticky="ew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text=("""NetControl application"""), font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Credits",
                            command=lambda: controller.show_frame(AppDetails))
        button1.pack()

        button2 = ttk.Button(self, text="Block Apps",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

        pTable = getProcessTable()
        # graphContainer = tk.Frame(self,  height = 480)
        # graphContainer.grid(row=0, column=0, sticky="ew")

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # graphContainer.pack(fill=None, expand=False)

        frame2 = tk.Frame(self, width=50, height = 50, background="#bbbbbb")
        # frame2.place(relx=.5, rely=.5, anchor="c")
        hj(frame2,"Chrome")
        for i in pTable:
            hj(frame2,i[:-4])
        frame2.pack(fill=None, expand=True)


        # hj(self,"Chrome")
        # for i in pTable:
        #     hj(self,i[:-4])


def hj(s, ProcessName):
    # ProcessName = "Chrome" , say
    label = tk.Label(s, text=ProcessName, font=SMALL_FONT)
    label.pack(pady=10,padx=10)
    #
    # list.add(label)
    # Process Path
    # label2 = tk.Label(s, text=getProcessPathByName(ProcessName), font=SMALL_FONT)
    # label2.pack(pady=10,padx=10)
    # self.buttonframe = Frame(self.root)
    # self.buttonframe.grid(row=2, column=0, columnspan=2)
    # Button(self.buttonframe, text = "Brighten").grid(row=0, column=0)
    # Button(self.buttonframe, text = "Darken").grid(row=0, column=1)

    buttonB = ttk.Button(s, text="Block", command=lambda: Block(ProcessName))
    buttonB.pack()
    buttonU = ttk.Button(s, text="Unblock", command=lambda: Unblock(ProcessName))
    buttonU.pack()

def hj(s, ProcessName):
    # ProcessName = "Chrome" , say
    label = tk.Label(s, text=ProcessName, font=SMALL_FONT)
    label.pack(pady=10,padx=10)

    buttonB = ttk.Button(s, text="Block", command=lambda: Blocker(s, ProcessName))
    buttonB.pack()
    buttonU = ttk.Button(s, text="Unblock", command=lambda: Unblocker(s,ProcessName))
    buttonU.pack()

def Blocker(s, pName):
    Block(pName)
    s.config(background="#b22222")

def Unblocker(s, pName):
    Unblock(pName)
    s.config(background="#22b222")

class AppDetails(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text=("""NetControl application"""), font=LARGE_FONT)
        label1.pack(pady=10,padx=10)

        label2 = tk.Label(self, text=("""Created by:\n Ambar Zaidi\nDeptt. of Computer Science & Engineering, IIT Roorkee
Bachelor of Technology (II Year)\n
Contact Details:
Enr. No.: 14114009
E-mail: ambar.ucs2014@iitr.ac.in"""), font=SMALL_FONT)
        label2.pack(pady=10,padx=10)

        # label = tk.Label(self, text=("""Created by: Ambar Zaidi\nBachelor of Technology,II Year
        #  \nDeptt. of Computer Science & Engineering,\n
        #  IIT Roorkee\n
        #  \nEnr. No.: 14114009
        #  \nE-mail: ambar.ucs2014@iitr.ac.in"""), font=SMALL_FONT)
        # label.pack(pady=10,padx=10)

        # ProcessName = "Chrome"
        # label = tk.Label(self, text=ProcessName, font=LARGE_FONT)
        # label.pack(pady=10,padx=10)
        # buttonB = ttk.Button(self, text="Block",
        #                     command=lambda: Block(ProcessName))
        # buttonB.pack()
        # buttonU = ttk.Button(self, text="Unblock",
        #                     command=lambda: Unblock(ProcessName))
        # buttonU.pack()
        button1 = ttk.Button(self, text="Close",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Running Applications", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        pTable = getProcessTable()

        # frame2.config(background="#22b222")
        # frame2.place(relx=.5, rely=.5, anchor="c")
        # hj(frame2,"Chrome")
        AppsContainer=tk.Frame(self, width=250,  background="#bbbbbb")
        for i in pTable:
            frame2 = tk.Frame(self, width=250, height = 80, background="#b22222")
            frame2.config(background="#22b222")
            hj(frame2,i[:-4])
            frame2.pack(fill=None, expand=False)
        AppsContainer.pack(fill=None, expand=False)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(padx=10, pady=20)


class BTCe_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(AppDetails))
        button1.pack()

        # canvas = FigureCanvasTkAgg(f, self)
        # canvas.show()
        # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        #
        # toolbar = NavigationToolbar2TkAgg(canvas, self)
        # toolbar.update()
        # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = NetControlApp()
app.geometry("1280x960")
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
