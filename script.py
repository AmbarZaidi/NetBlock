from sys import argv
from Tkinter import *
from PIL import Image, ImageTk, ImageFilter
import random

script, infile = argv

class MyApp(object):
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("ImagePro")



        #Original
        original = Image.open(infile)
        (w, h) = (original.size[0], original.size[1])
        tkpi = ImageTk.PhotoImage(original)
        label = Label(self.root, image=tkpi)
        label.grid(row =0, column=0, padx=5,pady=5)

        img = original.copy().convert("L")
        tkpi2 = ImageTk.PhotoImage(img)
        label = Label(self.root, image=tkpi2)
        label.grid(row =0, column=1, padx=5,pady=5)

        Label(self.root, text = "Original").grid(row=1, column=0)
        Label(self.root, text = "Modified").grid(row=1, column=1)
        Button(self.root, text = "Brighten").grid(row=2, column=0, sticky=W)
        Button(self.root, text = "Darken").grid(row=2, column=0, sticky=W, padx=60)
        Button(self.root, text = "Warm").grid(row=2, column=0, sticky=W, padx=112)
        Button(self.root, text = "Cool").grid(row=2, column=0, sticky=W, padx=158)








        self.root.mainloop()




MyApp()
