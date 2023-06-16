import cv2
import os
from sklearn.utils import shuffle
from tqdm import tqdm
import tensorflow as tf
 
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

model = tf.keras.models.load_model("oranges-cnn.model")

IMG_SIZE = 50
def prepare(filepath):
    # img_array = cv2.imread(filepath)
    # plt.imshow(filepath, cv2.IMREAD_COLOR)
    # plt.show()
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    # plt.imshow(img_array)
    # plt.show()    
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    # plt.imshow(new_array)
    # plt.show()
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

DATADIR = 'TEST DATASET'
CATAGORIES = ["freshoranges", "rottenoranges"]
path = os.path.join(DATADIR,CATAGORIES[0])  #tested all rotten

for img in os.listdir(path)[40:45]:
  prediction = model.predict([ prepare(path + '/' + str(img) )])
  print(img)
  if int(prediction[0][1]) == 1:
    print("--> ROTTEN\n")
  else:
    print("\n--> FRESH\n")
