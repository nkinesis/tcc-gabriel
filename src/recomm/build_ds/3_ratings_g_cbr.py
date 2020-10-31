#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from numpy import array
from numpy import argmax
from keras.models import load_model
from sklearn.preprocessing import OrdinalEncoder

def g_cbr(all_products, general, by_client, clients, rated_ds):
    # checar condições rating 1 e 2
    for client in clients:
        print("Avaliações 1 e 2, analisando cliente: " + str(client))
        filtered_by_client = by_client[by_client.client_id == client]
        client_products = filtered_by_client['product_id'].values
        for product in client_products:
            is_product_best_seller = general[(general.product_id == product)]
            if len(is_product_best_seller) > 0:
                # já comprou, é best seller no geral
                rated_ds.append([client, product, 2])
            else:
                # já comprou, não é best seller no geral
                rated_ds.append([client, product, 1])

    # checar condições rating 4
    best_seller_products = general['product_id'].values
    for client in clients:
        print("Avaliação 4, analisando cliente: " + str(client))
        filtered_by_client = by_client[by_client.client_id == client]
        client_products = filtered_by_client['product_id'].values
        top_but_not_bought = set(best_seller_products) - set(client_products)
        for product in top_but_not_bought:
            # não comprou, é best seller no geral
            rated_ds.append([client, product, 4])

    # checar condições rating 3
    rated = pd.DataFrame(rated_ds, columns=[
                         'client_id', 'product_id', 'rating'])
    products_not_included = set(all_products['product_id']) - set(rated['product_id'])
    for client in clients:
        print("Avaliação 3, analisando cliente: " + str(client))
        for product in products_not_included:
            # não comprou, não é best seller no geral
            rated_ds.append([client, product, 3])

if __name__ == "__main__":

    # carregar produtos únicos
    url = './unique_products.csv'
    all_products = pd.read_csv(url, delimiter=',')

    # carregar mais vendidos no geral
    url = './best_selling_general.csv'
    general = pd.read_csv(url, delimiter=',')

    # carregar mais vendidos por cliente
    url = './best_selling_by_client.csv'
    by_client = pd.read_csv(url, delimiter=',')

    # definir pontuação para cada par cliente/produto
    rated_ds = []
    clients = np.unique(by_client['client_id'])

    # designa os ratings
    g_cbr(all_products, general, by_client, clients, rated_ds)

    # compilar e salvar ratings no disco
    rated = pd.DataFrame(rated_ds, columns=[
                         'client_id', 'product_id', 'rating'])
    rated.to_csv('./g_cbr_aux.csv', index=False)

    # carregar ratings recém salvos
    url = './g_cbr_aux.csv'
    ratings = pd.read_csv(url, delimiter=',')

    # encodar produtos e clientes, ordinal encoding
    # cada registro passa a ser identificado por 1 inteiro
    print('Encodando produtos/clientes...')
    encoder = OrdinalEncoder()
    encoded_products = encoder.fit_transform(
        ratings['product_id'].values.reshape(-1, 1))
    encoded_clients = encoder.fit_transform(
        ratings['client_id'].values.reshape(-1, 1))

    ratings['product_id'] = encoded_products
    ratings['product_id'] = ratings['product_id'].astype('int32')

    ratings['client_id'] = encoded_clients
    ratings['client_id'] = ratings['client_id'].astype('int32')

    # salvar produtos encodados
    print('Salvando mapa de encoding...')
    encoded_products = encoder.fit_transform(
        all_products['product_id'].values.reshape(-1, 1))
    all_products['encoded_id'] = encoded_products
    all_products.to_csv('./unique_products_encoded.csv', index=False)

    # salvar ratings encodados
    ratings.to_csv('./g_cbr.csv', index=False)
    print("Concluído.")
