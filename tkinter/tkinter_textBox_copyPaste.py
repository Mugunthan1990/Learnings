import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("text box")
aLabel = ttk.Label(win, text ='Enter File Name' )
aLabel.grid(column = 0, row = 0)

def clickMe():
    file_name = name.get()
    with open(file_name) as File:
        f = File.read()

    action.configure(text = f)
    aLabel.configure(foreground = 'green')

action = ttk.Button(win, text = "Click me",  command = clickMe)
action.grid(column = 1, row = 1)

name = tk.StringVar() # initiate calss to ask for entry
textbox = ttk.Entry(win , width = 12, textvariable = name)
textbox.grid(column = 0, row = 1)




win.mainloop()
