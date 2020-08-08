#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

url = r'C:\temp\tcc-gabriel\data\olist-processed\new2.csv'
original_items = pd.read_csv(url, sep=',')
items_filtered_cols = original_items[['encoded_id', 'order_approved_at_month', 'product_id']]

unique_products = np.unique(items_filtered_cols[['product_id']].values)
len(unique_products)

items_filtered_cols['product_id'] = items_filtered_cols['product_id'].astype('category')

items_filtered_cols['product_id'] = items_filtered_cols['product_id'].cat.codes

count = pd.value_counts(items_filtered_cols['product_id'].values)
count.reset_index().values.tolist()

items_filtered_cols = items_filtered_cols[:10]
dum_df = pd.get_dummies(items_filtered_cols, columns=["product_id"], prefix=["product"] )

dum_df.to_csv(r'C:\temp\tcc-gabriel\data\olist-1000-onehot.csv')

items_filtered_cols.to_csv(r'C:\temp\tcc-gabriel\data\olist-1000-ordinal.csv')

dum_df.to_csv(r'C:\Users\ullma\Desktop\olist-10-onehot.csv')




