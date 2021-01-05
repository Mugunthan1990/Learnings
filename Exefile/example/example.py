from tkinter import *
from PIL import ImageTk
from PIL import Image
from tkinter import filedialog

root = Tk()
root.title("open image")
def Open():
    global my_image
    root.filename =  filedialog.askopenfilename( initialdir = "/media/einche/505C70FF5C70E0E0/Python fun programing/Learnings/Exefile/example", title = "Select a Image" , filetypes=(('png files', "*.png"), ("all file" , "*.*")))
    my_label = Label(root, text = root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image = my_image).pack()

my_btn = Button(root, text= "open file", command = Open).pack()

root.mainloop()

#im = Image.open("01.jpeg")
#im.show()
