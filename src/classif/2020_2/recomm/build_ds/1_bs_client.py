#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from numpy import array
from numpy import argmax
from keras.models import load_model

# definir quantos produtos serão considerados
top_x = 10

# carregar arquivo, substituir NaNs por 0, cast para int
url = '/home/ullmann/tcc-gabriel/data/uci-online-retail-source/online_retail.csv'
retail = pd.read_csv(url, delimiter=',')
retail = retail.fillna(0)
retail['clientId'] = retail['clientId'].astype('int32')

# contar clientes únicos
client_list = np.unique(retail['clientId'])

# contar produto mais vendido por cliente
best_selling_by_client = []
countc = 0
for client in client_list:
    filtered = retail[retail.clientId == client]
    best_selling = filtered['modeProd'].value_counts() 
    count = 0
    countc += 1
    print(countc)
    for product in best_selling.keys():
        filtered = retail[retail.clientId == client]
        best_selling_by_client.append([client, filtered.values[0][7], product])
        if count < top_x: # top X
            count += 1
        else:
            count = 0
            break

# salvar mais vendidos por cliente
df = pd.DataFrame(best_selling_by_client, columns=['client_id', 'country', 'product_id'])
df.to_csv('./best_selling_by_client.csv', index=False)  

# salvar produtos únicos
prods = np.unique(retail['modeProd'])
prods = pd.DataFrame(prods, columns=['product_id'])
prods.to_csv('./unique_products.csv', index=False)