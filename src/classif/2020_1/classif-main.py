#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import tensorflow as tf
from numpy import savetxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

# Function which will be used to compare prediction results
# See more on comment "Test predictions"
def countPositionOne(array, verbose):
    count = 0
    for col in array:
        if col == 1:
            if verbose:
                print(str(count) + " / " + str(len(array)))
            return count;
        count += 1
    if verbose:
        print("Not found.")
    return -1

# Load and divide dataset columns
url = 'C:/temp_ml_data/olist-3192-onehot.csv'
data = pd.read_csv(url, delimiter=',')
entradas=data.iloc[:,1:3]
saidas = data.iloc[:,3:916]
entradas=np.array(entradas)
saidas=np.array(saidas)

# Do train/test split
e_train, e_test, s_train, s_test = train_test_split(entradas, saidas, test_size=0.33, random_state=40)

# Create model object
model = Sequential()

model.add(Dense(units=64, activation='relu', input_dim=2))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

# Train and evaluate
model.fit(e_train, s_train,
          batch_size=10,
          epochs=1000,
          verbose=1,
          validation_data=(e_test, s_test),
         use_multiprocessing= True)
          
model.evaluate(e_test, s_test, verbose=0)

# View information about model
# model.summary()

# Test predictions
y=model.predict(entradas[:1000])
predictions = np.round(y)

# Predict and count sucess/error
p_success = 0
p_error = 0
verbose = True
for n in range(1, 1000):
    originalResult = countPositionOne(saidas[n], verbose)
    predictedResult = countPositionOne(predictions[n], verbose)
    if verbose:
        print("===")
    if (originalResult == predictedResult):
        p_success += 1
    else:
        p_error += 1
print("Successful predictions: " + str(p_success))
print("Wrong predictions: " + str(p_error))



