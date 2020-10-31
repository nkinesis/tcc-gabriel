import sys
from model.database import Database
from model.dataframe import Dataframe
from model.clustering import Clustering

def main():

    # create object instances
    print("Preparing to start...")
    print("Number of clusters: " + sys.argv[1])

    db = Database(None)
    df = Dataframe(None)
    n_clusters = int(sys.argv[1])
    cluster = Clustering(n_clusters if n_clusters else 1)

    # do db setup before starting (optional)
    cleandb = True
    if cleandb:
        db.clear("tcc", "processed")

    try:
        # get data
        print("Step 1/3 - Fetching and formatting...")
        to_cluster = {}
        rs = db.doQuery("tcc", "online_retail", to_cluster)

        # convert to dataframe and format
        orders = df.createDf(rs)
        orders = df.deleteCol(orders, "_id")
        # orders = df.deleteCol(orders, "avgQty")
        orders = df.convertDf(orders, "int32")

        #clusterize
        print("Step 2/3 - Clustering...")
        results = cluster.doKmeans(orders)

        # add clusterization results to dataset and save
        print("Step 3/3 - Preparing and saving...")
        orders = df.addCol(orders, "cluster", results["yhat"])
        orders_json = df.toJson(orders, False)
        result = db.insertMany("tcc", "processed", orders_json)
        print("Done!")
        print(result)

    except Exception as ex:
        print("An error has occured!")
        print(ex)

if __name__ == "__main__":
    main()