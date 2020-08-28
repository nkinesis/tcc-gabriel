#!/usr/bin/env python
# coding: utf-8

import os
import sys
import numpy as np
import pandas as pd
import warnings
# import matplotlib.pyplot as plt

from keras.layers import Input, Embedding, Flatten, Dot, Dense, Concatenate
from keras.models import Model

warnings.filterwarnings('ignore')

# validate params
if len(sys.argv) < 1:
    sys.exit('Parâmetros obrigatórios: informe num de épocas')

if not sys.argv[1].isdigit():
    sys.exit('Num de épocas ' + sys.argv[1] + ' não é um valor inteiro.')

# 1 load
dataset = pd.read_csv('./gabriel_ratings2.csv')

# 2 train/test split
from sklearn.model_selection import train_test_split
train, test = train_test_split(dataset, test_size=0.2, random_state=42)

# 3 counting features
n_users = len(dataset.client_id.unique())
n_prods = len(dataset.product_id.unique())

# 4 embedding
# creating book embedding path
prod_input = Input(shape=[1], name="Prod-Input")
prod_embedding = Embedding(n_prods+1, 5, name="Prod-Embedding")(prod_input)
prod_vec = Flatten(name="Flatten-Prods")(prod_embedding)

# creating user embedding path
client_input = Input(shape=[1], name="Client-Input")
client_embedding = Embedding(n_users+1, 5, name="Client-Embedding")(client_input)
client_vec = Flatten(name="Flatten-Clients")(client_embedding)

# concatenate features
conc = Concatenate()([prod_vec, client_vec])

# add fully-connected-layers
fc1 = Dense(128, activation='relu')(conc)
fc2 = Dense(32, activation='relu')(fc1)
out = Dense(1)(fc2)

# 5 create model and compile it
model2 = Model([client_input, prod_input], out)
model2.compile('adam', 'mean_squared_error')

from keras.models import load_model

if os.path.exists('regression_model2.h5'):
    model2 = load_model('regression_model2.h5')
else:
    history = model2.fit([train.client_id, train.product_id], train.rating, epochs=int(sys.argv[1]), verbose=1)
    model2.save('regression_model2.h5')
    # plt.plot(history.history['loss'])
    # plt.xlabel("Epochs")
    # plt.ylabel("Training Error")

# 6 test
model2.evaluate([test.client_id, test.product_id], test.rating)

# 7 predict
predictions = model2.predict([test.client_id.head(10), test.product_id.head(10)])

[print(predictions[i], test.rating.iloc[i]) for i in range(0,10)]