import tkinter as tk
from tkinter import ttk
from sys import argv, exit

if argv[1:]:
    file_name = argv[1]
    file_name2 = argv[2]
    with open (file_name) as file:
        f = file.read()
else:
    print("Please enter file name at start program")
    exit(0)
print(f)
win = tk.Tk()
win.title("Copy ....")
aLabel = ttk.Label(win, text = 'copy {} to {}'.format(file_name, file_name2))
aLabel.grid(column = 0, row = 0)


def Copy():
    try:
        f2 = open(file_name2 , 'w')
        f2.write(f)
        # action.configure(f2.write(f))
        aLabel.configure(foreground = 'red')
        f2.close()
    except ValueError:
        print('ok')
        exit(0)

action = ttk.Button(win , text = "copy" , command = Copy)
action.grid(column = 1, row = 0)


win.mainloop()
