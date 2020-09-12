import pandas as pd
import numpy as np

# caminho para o ds base está definido em um arquivo por conveniência
# abrir arquivo e definir path
f = open("path.txt", "r")
url = f.read()

# carregar arquivo, substituir NaNs por 0, cast para int
source = pd.read_csv(url, delimiter=',')
source = source.fillna(0)
source['clientId'] = source['clientId'].astype('int32')
f.close()

# criar arrays auxiliares
countries = []
result = pd.DataFrame()

# contar produtos únicos
products = np.unique(source['product_id'])

# para cada produto, listar os países (categorias) para os quais houve venda do produto em questão
count = 0
for product in products:
    count += 1
    print("Analisando produto " + str(count) + "/" + str(len(products)))
    bought_in_countries = source[(source.product_id == product)]['country'].value_counts().keys()
    countries.append(",".join(bought_in_countries))

# montar novo ds e salvar
result['product_id'] = products
result['countries'] = countries
result.to_csv('./prods_by_country.csv', index=False)