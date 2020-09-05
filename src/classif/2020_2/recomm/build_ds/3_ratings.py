#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from numpy import array
from numpy import argmax
from keras.models import load_model
from sklearn.preprocessing import OrdinalEncoder

# carregar produtos únicos
url = './unique_products.csv'
all_products = pd.read_csv(url, delimiter=',')

# carregar mais vendidos por país
url = './best_selling_by_country.csv'
by_country = pd.read_csv(url, delimiter=',')

# carregar mais vendidos por cliente
url = './best_selling_by_client.csv'
by_client = pd.read_csv(url, delimiter=',')

# definir pontuação para cada par cliente/produto
# rating baseado nas regras descritas no estágio
rated_ds = []
clients = np.unique(by_client['client_id'])

# checar condições rating 3 e 2
for client in clients:
    print("Ratings 3 e 2, analisando cliente: " + str(client))
    filtered_by_client = by_client[by_client.client_id == client]
    current_country = filtered_by_client.values[0][1]
    client_products = filtered_by_client['product_id'].values
    for product in client_products:
        is_product_in_country = by_country[(by_country.country == current_country) & (by_country.product_id == product)]
        if len(is_product_in_country) > 0:
            rated_ds.append([client, product, 3])
        else:
            rated_ds.append([client, product, 2])

# checar condições rating 4
for client in clients:
    print("Rating 4, analisando cliente: " + str(client))
    filtered_by_client = by_client[by_client.client_id == client]
    current_country = filtered_by_client.values[0][1]
    filtered_by_country = by_country[(by_country.country == current_country)]
    country_products = filtered_by_country['product_id'].values
    client_products = filtered_by_client['product_id'].values
    top_but_not_bought = set(country_products) - set(client_products)
    for product in top_but_not_bought:
        rated_ds.append([client, product, 4])       

# checar condições rating 1
rated = pd.DataFrame(rated_ds, columns=['client_id', 'product_id', 'rating'])
products_not_included = set(all_products['product_id']) - set(rated['product_id'])
clients = np.unique(by_client['client_id'])
for client in clients:
    print("Rating 1, analisando cliente: " + str(client))
    for product in products_not_included:
        rated_ds.append([client, product, 1])

# compilar e salvar ratings no disco
rated = pd.DataFrame(rated_ds, columns=['client_id', 'product_id', 'rating'])
rated.to_csv('./gabriel_ratings.csv', index=False)  

# carregar ratings recém salvos
url = './gabriel_ratings.csv'
ratings = pd.read_csv(url, delimiter=',')

# encodar produtos e clientes, ordinal encoding
# cada registro passa a ser identificado por 1 inteiro
encoder = OrdinalEncoder()
encoded_products = encoder.fit_transform(ratings['product_id'].values.reshape(-1, 1))
encoded_clients = encoder.fit_transform(ratings['client_id'].values.reshape(-1, 1))

ratings['product_id'] = encoded_products
ratings['product_id'] = ratings['product_id'].astype('int32')

ratings['client_id'] = encoded_clients
ratings['client_id'] = ratings['client_id'].astype('int32')

# salvar ratings encodados
ratings.to_csv('./gabriel_ratings2.csv', index=False)
print("Concluído.")
