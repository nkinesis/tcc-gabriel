#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

url = r'C:\temp\tcc-gabriel\data\new2.csv'
original_items = pd.read_csv(url, sep=',')
items_filtered_cols = original_items[['encoded_id', 'order_approved_at_month', 'product_id']]
items_filtered_cols = items_filtered_cols[:100]
items_filtered_cols

dum_df = pd.get_dummies(items_filtered_cols, columns=["product_id"], prefix=["product"] )
dum_df

dum_df.to_csv(r'C:\temp\tcc-gabriel\data\new3.csv')




