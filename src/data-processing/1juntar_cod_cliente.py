#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

url1= r'C:\temp\tcc-gabriel\data\orders.csv'
data1= pd.read_csv(url1, sep=',')
data1

url2= r'C:\temp\tcc-gabriel\data\customers.csv'
data2= pd.read_csv(url2, sep=',')
data2

url3= r'C:\temp\tcc-gabriel\data\orders_items.json'
data3= pd.read_json(url3, encoding='utf-8')
data3['customer_id'] = None
data3


### Passos
# - Verificar se o customer_id existe na tabela orders
# - Se existe busca quais order_item são dessa order
# - Coloca no campo order.customer_id o customer_id relacionado

only_cust_ids = data2[['customer_id', 'customer_unique_id']].values
result_list = [];

counter = 0
for ids in only_cust_ids:
     # if order has customer
     result = data1[(data1.customer_id == ids[0])]
     order_w_cust = result.order_id.values[0]
    
     # if item has order
     result = data3[(data3.order_id == order_w_cust)]
     result = result.values
     if len(result) > 0:
         result_list.append([ids[0], ids[1], order_w_cust, result[0][1], result[0][2], result[0][3]]);
        
     counter = counter + 1
     if counter % 1000 == 0 :
        print(counter)

pd.DataFrame(result_list).to_csv(r'C:\temp\tcc-gabriel\data\new.csv')





