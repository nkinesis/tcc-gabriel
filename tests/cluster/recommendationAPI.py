import datetime
from model.dataframe import Dataframe
from model.recommend import Recommend
from bottle import Bottle, route, run, request, response

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

@app.route("/smartbuy", method=["POST"])
def getRecommendation():
    try:
        clientId = int(request.params.get("clientId"))
        month = int(request.params.get("month"))
        
        if (month < 1 or month > 12):
            return "Erro: mês inválido. Valor deve estar entre 1 e 12."
        
        if (clientId < 1):
            return "Erro: categoria inválida. Valor deve ser maior que zero."
        
        rc = Recommend("tcc", "processed")
        return rc.get(clientId, month)

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