import time
import tensorflow as tf
from keras.models import Sequential
import pandas as pd
from keras.layers import Dense
import numpy as np
from pymongo import MongoClient
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

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

# contar número de categorias para informar na saída
x = saidas['modeProd'].to_numpy()
saidas_units = len(np.unique(x))

# criar modelo sequencial do keras
model = Sequential()

# original: 64 units, relu, 2 inputs
model.add(Dense(units=64, activation='relu', input_dim=num_inputs))
model.add(Dense(units=saidas_units, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
model.fit(onehot_entradas, onehot_saidas,
          batch_size=10,
          epochs=1,
          verbose=1,
          validation_data=(onehot_entradas,onehot_saidas))

y=model.predict(onehot_entradas)
predicted = np.round(y)

# Salvar predições
counter = 0
timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
with open("./results" + timestamp + ".txt", 'w+') as f:
    for row in predicted:
        f.write("[")
        for position in row:
            f.write(" %s " % position)
        f.write("]\n")
print("Predictions saved.")

# Salvar modelo em hdf5 (Hierarchical Data Format)
model.save('./model' + timestamp + '.h5')
print("Model saved.")