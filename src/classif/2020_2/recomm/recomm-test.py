import os
import sys
import warnings
import numpy as np
import pandas as pd
from keras.models import Model
from keras.models import load_model
from sklearn.model_selection import train_test_split

warnings.filterwarnings('ignore')

# 1 validate params
# sys.argv[1] - Client ID
# sys.argv[2] - Product ID

if len(sys.argv) < 2:
    sys.exit('Parâmetros obrigatórios: informe intervalo inicial/final')

if not sys.argv[1].isdigit():
    sys.exit('Inicial ' + sys.argv[1] + ' não é um valor inteiro.')

if not sys.argv[2].isdigit():
    sys.exit('Final ' + sys.argv[2] + ' não é um valor inteiro.')

p_begin = int(sys.argv[1])
p_end = int(sys.argv[2])

# 2 load ds
dataset = pd.read_csv('./gabriel_ratings2.csv')

# 3 train/test split
train, test = train_test_split(dataset, test_size=0.2, random_state=42)

# 4 load model
if os.path.exists('regression_model2.h5'):
    model2 = load_model('regression_model2.h5')
else:
    print('Modelo regression_model2.h5 não encontrado.')

# 5 predict
predictions = model2.predict([
        test.client_id[p_begin:p_end], 
        test.product_id[p_begin:p_end]
    ])

# cv = test.client_id.values
# pv = test.product_id.values
lp = len(predictions)
[print(test.client_id.iloc[i], test.product_id.iloc[i], predictions[i if i < lp else lp-1], test.rating.iloc[i]) for i in range(p_begin,p_end)]