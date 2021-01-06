import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Copy paste")
aLabel = ttk.Label(win, text ='Enter File Name' )
aLabel.grid(column = 0, row = 0)

def clickMe():
    file_name = name.get()
    with open(file_name) as File:
        f = File.read()
    file_name2 = name2.get()
    f2 = open(file_name2, 'w')
    f2.write(f)
    f2.close()
    action.configure(text = f)
    aLabel.configure(foreground = 'green')

action = ttk.Button(win, text = "Click me",  command = clickMe)
action.grid(column = 1, row = 1)

name = tk.StringVar() # initiate calss to ask for entry
name2 = tk.StringVar() # initiate calss to ask for entry

textbox = ttk.Entry(win , width = 12, textvariable = name)
textbox.grid(column = 0, row = 1)
textbox = ttk.Entry(win , width = 12, textvariable = name2)
textbox.grid(column = 0, row = 2)





win.mainloop()
