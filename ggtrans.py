from cProfile import label
from tkinter import *
from googletrans import Translator
from PIL import Image, ImageTk

translator = Translator()

root = Tk()
root.title("Google Galaxy")
root.geometry("500x630")
root.iconbitmap("img+font\\logo.ico")

load = Image.open("img+font\\background.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image = render)
img.place(x = 0, y = 0)

name = Label(root, text = "Translator", fg = "#FFFFFF", bd = 0, bg = "#03152D")
name.config(font = ("Transformers Movie", 30))
name.pack(pady=10)

box_in = Text(root, width= 30, height= 8, font=("ROBOTO", 16))
box_in.pack(pady= 20)

button_frame = Frame(root).pack(side = BOTTOM)

def clear():
    box_in.delete(1.0, END)
    box_trans.delete(1.0, END)
def translate():
    inp = box_in.get(1.0, END)
    res = translator.translate(inp, dest='en', src='vi').text
    box_trans.delete(1.0, END)
    box_trans.insert(END, res)
clear_btn = Button(button_frame, text = "Clear Text", font = (("Aria"), 10, 'bold'), bg='#303030', fg = '#FFFFFF', command=clear)
trans_btn = Button(button_frame, text = "Translate", font = (("Aria"), 10, 'bold'), bg='#303030', fg = '#FFFFFF', command=translate)
clear_btn.place(x = 150, y = 310)
trans_btn.place(x = 290, y = 310)

box_trans = Text(root, width= 30, height= 8, font=("ROBOTO", 16))
box_trans.pack(pady= 50)

root.mainloop()