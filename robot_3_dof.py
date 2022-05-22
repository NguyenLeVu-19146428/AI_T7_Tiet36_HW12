# -*- coding: utf-8 -*-
"""Robot 3 Dof.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BN4MsSmhMQmFNt4P56NGuwWZeoyAfWVy
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

# Define Variables
l1 = 40
l2 = 50
l3 = 20
x_train = []
y_train = []
# Create Data
for t1 in np.linspace(-(2 * np.pi), 2 * np.pi, 100):
  for t2 in np.linspace(-(2 * np.pi), 2 * np.pi, 100):
    for t3 in np.linspace(-(2 * np.pi), 2 * np.pi, 100):
      x = l1*m.cos(t1) + l2*m.cos(t1+t2) + l3*m.cos(t1+t2+t3)
      y = l1*m.sin(t1) + l2*m.sin(t1+t2) + l3*m.sin(t1+t2+t3)
      beta = (t1 + t2 + t3)*180/3.14
      x_train.append(np.array([x,y,beta]))
      y_train.append(np.array([t1,t2,t3]))
# Convert to array
scaler = StandardScaler()
x_train = np.array(scaler.fit_transform(x_train))
y_train = np.array(y_train)
# Shuffe
x_train, y_train = shuffle(x_train, y_train)

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

model = Sequential()
model.add(Dense(256, activation='relu', input_shape = (3,)))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(3, activation='linear'))
model.compile(loss='mae', optimizer =tf.optimizers.Adam(learning_rate=0.0001))
history = model.fit(x_train, y_train, batch_size = 512, epochs = 10, validation_split = 0.2)
plot_reg_history(history)

test = scaler.transform(np.array([[60,0,45]]))
t1 = model.predict(test)[0][0]
t2 = model.predict(test)[0][1]
t3 = model.predict(test)[0][2]
x = l1*m.cos(t1) + l2*m.cos(t1+t2) + l3*m.cos(t1+t2+t3)
y = l1*m.sin(t1) + l2*m.sin(t1+t2) + l3*m.sin(t1+t2+t3)
beta = (t1 + t2 + t3)*180/3.14
print("Model dự đoán với giá trị đầu vào x = 90, y = 0 và beta = 45 là t1 = " + str(t1) + " t2 = "+ str(t2) + " t3 = "+ str(t3))
print("Kiểm tra: ")
print("Với giá trị t1 và t2 dự đoán ta tính lại x = " + str(x) + " y = "+ str(y)+ " beta = "+ str(beta))