# -*- coding: utf-8 -*-
"""Robot 2 Dof.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Pkk_rfawcvl4xcextAHDF_qbTSNEzhz
"""

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import StandardScaler
from keras.utils import np_utils
from sklearn.utils import shuffle
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pickle
import tensorflow as tf
import math as m

def plot_reg_history(history_fine):
  loss = history_fine.history['loss']
  val_loss = history_fine.history['val_loss']
  plt.subplot(2, 1, 2)
  plt.plot(loss, label='Loss')
  plt.plot(val_loss, label='Validation Loss')
  plt.legend(loc='upper right')
  plt.title('Loss')
  plt.xlabel('epoch')
  plt.show()

# Define Variables
l1 = 40
l2 = 50
x_train = []
y_train = []
# Create Data
for t1 in np.linspace(-(2 * np.pi), 2 * np.pi, 500):
  for t2 in np.linspace(-(2 * np.pi), 2 * np.pi, 500):
    x = l1*m.cos(t1) + l2*m.cos(t1+t2)
    y = l1*m.sin(t1) + l2*m.sin(t1+t2)
    x_train.append(np.array([x,y]))
    y_train.append(np.array([t1,t2]))
# Convert to array
scaler = StandardScaler()
x_train = np.array(scaler.fit_transform(x_train))
y_train = np.array(y_train)
# Shuffe
x_train, y_train = shuffle(x_train, y_train)

model = Sequential()
model.add(Dense(256, activation='relu', input_shape = (2,)))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(2, activation='linear'))
model.compile(loss='mae', optimizer =tf.optimizers.Adam(learning_rate=0.0001))
history = model.fit(x_train, y_train, batch_size = 512, epochs = 10, validation_split = 0.2)
plot_reg_history(history)

test = scaler.transform(np.array([[90,0]]))
t1 = model.predict(test)[0][0]
t2 = model.predict(test)[0][1]

x = l1*m.cos(t1) + l2*m.cos(t2+t1)
y = l1*m.sin(t1) + l2*m.sin(t2+t1)

print("Model d??? ??o??n v???i gi?? tr??? ?????u v??o x = 90 v?? y = 0 l?? t1 = " + str(t1) + " t2 = "+ str(t2))
print("Ki???m tra: ")
print("V???i gi?? tr??? t1 v?? t2 d??? ??o??n ta t??nh l???i x = " + str(x) + " y = "+ str(y))