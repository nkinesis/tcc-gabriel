#!/usr/bin/env python
# coding: utf-8

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import numpy as np

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

# contar produto mais vendido por cliente
best_selling_by_client = []
countc = 0
for client in client_list:
    filtered = retail[retail.clientId == client]
    best_selling = filtered['product_id'].value_counts() 
    count = 0
    countc += 1
    print("Analisando cliente " + str(countc) + "/" + str(len(client_list)))
    for product in best_selling.keys():
        filtered = retail[retail.clientId == client]
        #best_selling_by_client.append([client, filtered.values[0][7], product])
        search_idx = np.where(retail.columns.values == 'country')[0][0]
        best_selling_by_client.append([client, filtered.values[0][search_idx], product])
        if count < top_x: # top X
            count += 1
        else:
            count = 0
            break

# salvar mais vendidos por cliente
df = pd.DataFrame(best_selling_by_client, columns=['client_id', 'country', 'product_id'])
df.to_csv('./best_selling_by_client.csv', index=False)  

# salvar produtos únicos
prods = np.unique(retail['product_id'])
prods = pd.DataFrame(prods, columns=['product_id'])
prods.to_csv('./unique_products.csv', index=False)
print("Concluído.")