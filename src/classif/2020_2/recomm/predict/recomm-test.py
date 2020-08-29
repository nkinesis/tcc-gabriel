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
    sys.exit('Cliente ' + sys.argv[1] + ' não é um valor inteiro.')

if not sys.argv[2].isdigit():
    sys.exit('Produto ' + sys.argv[2] + ' não é um valor inteiro.')

p_client_id = int(sys.argv[1])
p_product_id = int(sys.argv[2])

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
inputs = [pd.Series([p_client_id], index =[1]), 
            pd.Series([p_product_id], index =[1])
         ]

predictions = model2.predict(inputs)
real = test[(test.client_id == p_client_id) & (test.product_id == p_product_id)]
real = real.values[0][2] if len(real) > 0 else None

if real:
    lp = len(predictions)
    print("=====")
    print("Rating previsto/real para o cli " + str(p_client_id) + " / prod " + str(p_product_id))
    [print(predictions[0], real)]
else:
    print("Par produto/cliente não encontrado.")