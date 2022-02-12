from tkinter import *
from tkinter.ttk import *
from time import strftime
import datetime

root = Tk()
root.title("Digital Clock")
colors = ["green", "blue", "white", "red"]
def clock():
    string = strftime('%H:%M:%S:%p')
    label.config(text = string, foreground=colors[datetime.datetime.now().second % 4])
    label.after(1000, clock)

label = Label(root, font = ("Courier New", 100), background= "black", foreground="green")
label.pack(anchor='center')
clock()

root.mainloop()