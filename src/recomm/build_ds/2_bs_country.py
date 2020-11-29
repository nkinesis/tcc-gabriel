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
retail = pd.read_csv(url.replace("\n", ""), delimiter=',')

# contar países únicos
country_list = np.unique(retail['country'])

# contar mais vendido por país
best_selling_by_country =[]
for country in country_list:
    filtered = retail[retail.country == country]
    best_selling = filtered['product_id'].value_counts()
    print(country + ": " + str(len(filtered)))
    
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
df.to_csv('./best_selling_by_country.csv', index=False)
print("Concluído.")