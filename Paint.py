from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

app = Tk()
app.geometry("400x400")

array1 = np.zeros((400,400))
xcoordlist = []
ycoordlist = []

def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw_smth(event):
    global lasx, lasy
    xcoordlist.append(lasx)
    ycoordlist.append(lasy)
    canvas.create_line((lasx, lasy, event.x, event.y), fill='black', width=2)
    lasx, lasy = event.x, event.y
    array1[event.x,event.y] = 1
    #print(event.x,event.y)


def plot_binary_array(array):
    plt.imshow(np.rot90(np.rot90(np.rot90(np.flip(array,0)))), cmap='binary', interpolation='nearest')
    plt.axis('off')
    plt.show()

def on_close():
    plot_binary_array(array1)
    print(xcoordlist)
    print(ycoordlist)
    app.destroy()


canvas = Canvas(app, bg='black')
canvas.pack(anchor='nw', fill='both', expand=1)

canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_smth)

image = Image.open("image.jpg")
image = image.resize((400,400))
image = ImageTk.PhotoImage(image)
canvas.create_image(0,0, image=image, anchor='nw')

app.protocol("WM_DELETE_WINDOW", on_close)

app.mainloop()