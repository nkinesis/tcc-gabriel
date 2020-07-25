from database import *
from dataframe import *
from clustering import *

def main():

    # do db setup before starting (optional)
    print("Preparing to start...")
    cleandb = True
    if cleandb:
        clear('tcc', 'processed')

    try:
        # get data
        print("Step 1/3 - Fetching and formatting...")
        rs = doQuery("tcc", "online_retail", { "avgQty": "2" })

        # convert to dataframe and format
        orders = createDf(rs)
        orders = deleteCol(orders, "_id")
        orders = deleteCol(orders, "avgQty")
        orders = convertDf(orders, "int32")

        #clusterize
        print("Step 2/3 - Clustering...")
        results = doKmeans(orders, 4)

        # add clusterization results to dataset and save
        print("Step 3/3 - Preparing and saving...")
        orders = addCol(orders, "cluster", results["yhat"])
        orders_json = toJson(orders)
        result = insertMany("tcc", "processed", orders_json)
        print("Done!")

    except Exception as ex:
        print("An error has occured!")
        print(ex)

if __name__ == "__main__":
    main()