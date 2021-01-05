import tkinter as tk
from tkinter import ttk # have butten facilities
import os
import webbrowser # It will open cross platform directories

# main window
win = tk.Tk()
win.title("python GUI")
# As long as user close this window will run in a lopp
win.resizable(0,0) # will lock the size int to perticuler size
aLabel = ttk.Label(win, text = "A Label")  # creating a Label instance
aLabel.grid(column = 0, row = 0) # defining which column and row the Label need to be apear

def openDir():
    action.configure(text  = "I ahave been clicked")
    aLabel.configure(foreground =   'red')
    path = r"C:\Users\TZ378YV\Dev\Learning"
    webbrowser.open(path) # It will open cross platform directories

    # path = os.path.realpath(path)  # Only work on windows
    # os.startfile(path)


action = ttk.Button(win, text = 'click me', command = openDir)
action.grid(column = 1, row = 0)





win.mainloop() #where the programme start running
