#!/usr/bin/env python
# coding: utf-8

import gc
import sys
import time
import pandas as pd
import numpy as np
from numpy import array
from numpy import argmax
import tensorflow as tf
from keras.layers import Dense
from keras.models import Sequential
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.utils import compute_class_weight

class MyCustomCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        gc.collect()

# carregar arquivo e formatar
url = './test-uci.csv'
data = pd.read_csv(url, delimiter=',')
data = data[['clientId', 'month', 'modeProd']]
entradas=data.iloc[:,0:2]
saidas = data.iloc[:,2:3]
entradas = entradas.astype("int32")
saidas = saidas.astype("int32")

# encodar entradas e saídas
onehot_saidas = pd.get_dummies(saidas.modeProd, prefix='prod')
onehot_entradas = pd.get_dummies(entradas.clientId, prefix='client')
num_inputs = len(onehot_entradas.columns) + 1
onehot_entradas['month'] = entradas.month
onehot_entradas = onehot_entradas.astype('uint8')

# computar balanceamento de classes
saidas_list = list(onehot_saidas.values)
y_integers = np.argmax(saidas_list, axis=1)
y_labels = np.unique(y_integers)
classWeight = compute_class_weight('balanced', y_labels, y_integers)
classWeight = dict(enumerate(classWeight))

# contar número de categorias para informar na saída
saidas_units = len(y_labels)

# criar modelo sequencial do keras
model = Sequential()

# original: 64 units, relu
model.add(Dense(units=64, activation='relu', input_dim=num_inputs))
model.add(Dense(units=saidas_units, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
history = model.fit(onehot_entradas, onehot_saidas,
          batch_size=int(sys.argv[1]),
          epochs=int(sys.argv[2]),
          verbose=1,
          validation_data=(onehot_entradas,onehot_saidas),
          callbacks=[MyCustomCallback()],
          class_weight=classWeight)

# Salvar estatísticas
timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
acc_size = len(history.history['accuracy'])
loss_size = len(history.history['loss'])
with open("./results" + timestamp + ".txt", 'w+') as f:
    f.write(str(history.history['accuracy'][acc_size-1]))
    f.write(";")
    f.write(str(history.history['loss'][acc_size-1]))
print("Results saved.")

# Salvar modelo em hdf5 (Hierarchical Data Format)
model.save('./model' + timestamp + '.h5')
print("Model saved.")