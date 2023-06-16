import os
import cv2
import matplotlib.pyplot as plt
from tkinter import * 
from PIL import Image, ImageTk

import cv2
import os
from sklearn.utils import shuffle
from tqdm import tqdm
import tensorflow as tf
import tkinter as tk
 
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from tkinter import filedialog

root  = Tk()
root.title("Oranges Classification")

IMG_SIZE = 50
def prepare(filepath):
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)  
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

path = "D:\\SEM-5\\_CHE1017 (FPE)\\Project\\fpe\\_oranges\\"
model = tf.keras.models.load_model("oranges-cnn.model")
def output(img_path):
    global result_label
    prediction = model.predict([ prepare(path + str(img_path) )])
    result = ""
    pred = prediction[0][1]
    pred_p = int(pred*100)
    if int(pred) == 1:
        result = "ROTTEN Orange"
        root.configure(background='red')

    else:
        result = "FRESH Orange"
        root.configure(background='green')
        # result_label.config(bg= "green")
    return result

images=os.listdir(path)
img_list = []
for img in images:
    myimg = ImageTk.PhotoImage(Image.open(path + img))
    img_list.append(myimg)

def selectFolder():
    folder = filedialog.askdirectory(initialdir="D:\\SEM-5\\_CHE1017 (FPE)\\Project\\fpe\\")
    global img_list
    global images
    global path
    global my_label
    global button_next
    global button_back

    if folder:
        path = folder + '/'
        print("\n", folder, "\n")
        img_list = []
        images = os.listdir(path)
        for img in images:
            myimg = ImageTk.PhotoImage(Image.open(path + img))
            img_list.append(myimg)
 
my_image1 = ImageTk.PhotoImage(Image.open(path+ images[0]))
result = output(images[0])

my_label = Label(image=my_image1)
result_label = Label(text=result, font=14)
cur_dir = Label(text=path, font=8)

my_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

result_label.grid(row=1, column=0, columnspan=3, pady=10)
cur_dir.grid(row=3, column=0, columnspan=3, pady=20)

def next(image_number):
    global my_label
    global button_next
    global button_back
    global result_label
    global cur_dir

    my_label.grid_forget()
    my_label = Label(image=img_list[image_number-1])
    button_next = Button(root, text=">>", command=lambda: next(image_number+1), font = 14)
    button_back = Button(root, text="<<", command=lambda: back(image_number-1), font = 14)

    if image_number == len(images):
        button_next = Button(root, text=">>", state=DISABLED, font = 14)

    my_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
    button_back.grid(row=1, column=0, padx=100)
    button_next.grid(row=1, column=2, padx=100)

    result = output(images[image_number-1])
    result_label.after(1, result_label.destroy())

    result_label = Label(text=result, font = 14)
    result_label.grid(row=1, column=0, columnspan=3, pady=10)
    # result_label.config(bg= "gray51", fg= "white")
    
    cur_dir.after(1, cur_dir.destroy())
    cur_dir = Label(text=path, font=8)
    cur_dir.grid(row=3, column=0, columnspan=3, pady=20)

def back(image_number):
    global my_label
    global button_next
    global button_back
    global result_label
    global cur_dir

    my_label.grid_forget()
    my_label = Label(image=img_list[image_number-1])
    button_next = Button(root, text=">>", command=lambda: next(image_number+1), font=14)
    button_back = Button(root, text="<<", command=lambda: back(image_number-1), font=14)
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED, font=14)
    my_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
    button_back.grid(row=1, column=0, padx=100)
    button_next.grid(row=1, column=2, padx=100)

    result = output(images[image_number-1])
    result_label.after(1, result_label.destroy())
    result_label = Label(text=result, font=14)
    result_label.grid(row=1, column=0, columnspan=3, pady=10)
    # result_label.config(bg= "gray51", fg= "white")

    cur_dir.after(1, cur_dir.destroy())
    cur_dir = Label(text=path, font=8)
    cur_dir.grid(row=3, column=0, columnspan=3, pady=20)


button_back = Button(root, text="<<", command=lambda: back, state=DISABLED, font=14)
button_back.grid(row=1, column=0)

button_next = Button(root, text=">>", command=lambda: next(2), font=14)
button_next.grid(row=1, column=2)

button_dir = Button(root, text="Choose directory", command=selectFolder)
button_dir.grid(row=2, column=1, pady=20)


root.mainloop()