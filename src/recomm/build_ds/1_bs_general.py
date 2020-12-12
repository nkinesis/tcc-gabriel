#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from numpy import array
from numpy import argmax
# from keras.models import load_model

# definir quantos produtos serão considerados
top_x = 10

# caminho para o ds base está definido em um arquivo por conveniência
# abrir arquivo e definir path
f = open("path.txt", "r")
url = f.read()

# carregar arquivo, substituir NaNs por 0, cast para int
retail = pd.read_csv(url.replace("\n", ""), delimiter=',')
retail = retail.fillna(0)
retail['clientId'] = retail['clientId'].astype('int32')

# contar clientes únicos
client_list = np.unique(retail['clientId'])

# contar produto mais vendido no geral
count_result = retail['product_id'].value_counts()[:top_x]
df = pd.DataFrame()
df['product_id'] = count_result.keys()
df['qty'] = count_result.values

# salvar mais vendidos no geral
df.to_csv('./best_selling_general.csv', index=False)  

# salvar produtos únicos
prods = np.unique(retail['product_id'])
prods = pd.DataFrame(prods, columns=['product_id'])
prods.to_csv('./unique_products.csv', index=False)
print("Concluído.")