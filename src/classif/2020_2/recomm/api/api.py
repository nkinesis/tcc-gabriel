import json
import math
import datetime
import pandas as pd
from keras.models import Model
from keras.models import load_model
from bottle import Bottle, route, run, request, response

# carregar produtos únicos
url = '../build_ds/unique_products_encoded.csv'
all_products = pd.read_csv(url, delimiter=',')

app = Bottle()
@app.hook("after_request")
def enable_cors():
    """
    You need to add some headers to each request.
    Don"t use the wildcard "*" for Access-Control-Allow-Origin in production.
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "PUT, GET, POST, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token"

@app.route("/test", method=["OPTIONS", "POST"])
def hello():
    return "O servidor está online! Data/hora atual: " + str(datetime.datetime.now())  

@app.route("/getEncodedRating", method=["POST"])
def getRating():
    try:
        clientId = int(request.params.get("clientId"))
        productId = int(request.params.get("productId"))
        
        if productId < 1:
            return "Erro: ID Produto inválido. Valor deve ser maior que zero."
        
        if clientId < 1:
            return "Erro: ID Cliente inválido. Valor deve ser maior que zero."
        
        inputs = [pd.Series([clientId], index=[1]), 
                  pd.Series([productId], index=[1])
                ]
        model2 = load_model('../predict/regression_model2.h5')
        predictions = model2.predict(inputs)

        if len(predictions) > 0:
            return str(math.ceil(predictions[0]))
        else:
            return 0

    except Exception as ex:
        print(ex)
        return str(ex)

@app.route("/getRatings", method=["POST"])
def getRatings():
    try:

        if not request.params.get("clientId").isdigit():
            return "Erro: ID Cliente inválido. Valor deve ser inteiro."

        clientId = int(request.params.get("clientId"))
        productIds = request.params.get("productIds").split(",")

        if clientId < 1:
            return "Erro: ID Cliente inválido. Valor deve ser maior que zero."

        if len(productIds) < 1 or len(productIds) > 5:
            return "Erro: Informe entre 1 e 5 IDs de produto."

        model2 = load_model('../predict/regression_model2.h5')
        result = []

        for product in productIds:
            filtered = all_products[(all_products.product_id == product)]
        
            if len(filtered) > 0:
                inputs = [pd.Series([clientId], index=[1]), 
                        pd.Series([filtered.values[0][1]], index=[1])
                        ]
                predictions = model2.predict(inputs)
                processed_value = math.ceil(predictions[0])
            else:
                predictions = []
                processed_value = 0

            if len(predictions) > 0:
                result.append({
                                'product_id': product, 
                                'rating': processed_value
                              })
            else:
                result.append({
                                'product_id': product, 
                                'rating': 0
                              })

        return json.dumps(result)

    except Exception as ex:
        print(ex)
        return str(ex)

if __name__ == "__main__":
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("--host", dest="host", default="localhost",
                      help="hostname or ip address", metavar="host")
    parser.add_option("--port", dest="port", default=8080,
                      help="port number", metavar="port")
    (options, args) = parser.parse_args()
    run(app, host=options.host, port=int(options.port))

# run(host="localhost", port=8080, debug=True)