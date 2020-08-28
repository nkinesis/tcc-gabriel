#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from numpy import array
from numpy import argmax
from keras.models import load_model

# definir quantos produtos serão considerados
top_x = 10

# carregar
url = '/home/ullmann/tcc-gabriel/data/uci-online-retail-source/online_retail.csv'
retail = pd.read_csv(url, delimiter=',')

# contar países únicos
country_list = np.unique(retail['country'])

# contar mais vendido por país
best_selling_by_country =[]
for country in country_list:
    filtered = retail[retail.country == country]
    best_selling = filtered['modeProd'].value_counts()
    #print(country + ": " + str(len(filtered)))
    
    count = 0
    for product in best_selling.keys():
        best_selling_by_country.append([country, product])
        if count < top_x: # top X
            count += 1
        else:
            count = 0
            break

# slavar mais vendidos por país
df = pd.DataFrame(best_selling_by_country, columns=['country', 'product_id'])
df.to_csv('C:/Users/Gabriel Ullmann/Desktop/best_selling_by_country.csv', index=False)