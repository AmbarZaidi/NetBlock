import Tkinter as tk
from Tkinter import *

class ProcessDiv(Frame):
    """A GUI application with button and label """
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.button_clicksB = 0 #counts the number of button clicks
        self.button_clicksU = 0 #counts the number of button clicks
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, text = "ProcessName")
        self.label.grid()

        self.buttonB = Button(self)
        self.buttonB["text"]="Block"
        self.buttonB["command"] = self.update_countB
        self.buttonB.grid()

        self.buttonU = Button(self)
        self.buttonU["text"]="Unblock"
        self.buttonU["command"] = self.update_countU
        self.buttonU.grid()


    def update_countB(self):
        self.button_clicksB += 1
        self.buttonB["text"] = "Block: "+str(self.button_clicksB)

    def update_countU(self):
        self.button_clicksU += 1
        self.buttonU["text"] = "Unblock: "+str(self.button_clicksU)

root = Tk()
root.title("NetBlock")
root.geometry("200x150")

app = ProcessDiv(root)

root.mainloop()
