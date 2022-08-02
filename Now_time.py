from tkinter import *
from tkinter.ttk import*
from time import strftime

r = Tk()
r.title("Time")
def t():
    s = strftime("%H:%M:%S %p")
    label.config(text=s)
    label.after(1000, t)
label=Label(r, font=("ds.digital", 80), background="black", foreground="red" )
label.pack(anchor="center")
t()

mainloop()
