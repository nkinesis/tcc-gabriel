from model.database import Database
from model.dataframe import Dataframe

class Recommend:
    def __init__(self, database, collection):
        self.db = database
        self.coll = collection

    def get(self, clientId, month):
        db = Database(None)
        df = Dataframe(None)

        query = { "clientId": clientId, "month": month }
        result = db.doQuery(self.db, self.coll, query)
        orders = df.createDf(result)

        if len(result) > 0:
            orders = df.deleteCol(orders, "_id")

        return df.toJson(orders, True)

if __name__ == "__main__":
    print("Recommendation test.")
    #rc = Recommend("tcc", "processed")
    #rc.get(13047, 1)