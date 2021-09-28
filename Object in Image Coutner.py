#pip install pillow, image, tkinter
import tkinter as tk
from tkinter import *
from tkinter import Tk, Label, ttk, filedialog, Button
from PIL import ImageTk, Image
import image
import os

# global variables
count = 0
img_id=0


# counter function
def clicked(): 
    global count

    count = count + 1

    label1.configure(text=f'Image has {count} instances.')






root = Tk()
root.title("Count inside image")
root.geometry("550x600+700+200")
root.resizable(width=True, height=True)

panel = Button(root, width=600 , height=600,command=clicked)
# c = Canvas(root, width=510,height=510,bg='black')


c = Canvas(panel,width=500,height=500, bg = 'black')
c.pack()



def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def open_img():
    panel.pack()
    x = openfn()
    global count
    global img_id

    count = 0
    img = Image.open(x)
    img = img.resize((450, 450), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img_id = c.create_image((0,0),image=img)
    
    c.itemconfig(img_id, image=img)
    
    
    
    






topLabel = Label(root, text=" " )


label1 = tk.Label(root)
label1.pack()

topLabel.pack()
btn = Button(root, text='Image To Count', command=open_img).pack()


root.mainloop()