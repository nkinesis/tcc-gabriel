#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

url = r'C:\temp\tcc-gabriel\data\new.csv'
original_items = pd.read_csv(url, sep=',')
items_filtered_cols = original_items[['customer_unique_id', 'order_approved_at_month', 'product_id']]
items_filtered_cols[:3]

items_filtered_cols_unq = items_filtered_cols[['customer_unique_id']].values
items_filtered_cols_unq = pd.DataFrame(items_filtered_cols_unq, columns = ['cust_id'])
items_filtered_cols_unq['index'] = np.arange(1, len(items_filtered_cols_unq)+1) 
items_filtered_cols_unq

len(items_filtered_cols)

counter = 0
items_arr = items_filtered_cols.values
newArr = []
for item in items_arr:
    rs = items_filtered_cols_unq[(items_filtered_cols_unq.cust_id == item[0])]
    newIdx = rs['index'].values[0]
    newArr.append([item[0], newIdx, item[1], item[2]])
    counter = counter + 1
    if counter % 1000 == 0 :
        print(counter)

pd.DataFrame(newArr).to_csv(r'C:\temp\tcc-gabriel\data\new2.csv')



