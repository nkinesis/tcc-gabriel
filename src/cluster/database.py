from pymongo import MongoClient
import pandas as pd
import numpy as np

class Database:    
    
    def __init__(self, connStr):
        self.connStr = connStr if connStr else "mongodb://localhost:27017"

    def getConnection(self, type):
        try:
            client = MongoClient(self.connStr)
            db = client.admin
            status = db.command("serverStatus")
            if not type or type == "test":
                return status
            else:
                return client
        except Exception as ex:
            print(ex)
            return None

    def doQuery(self, db, document, query):
        try:
            client = self.getConnection(True)
            mydb = client[db]
            mycol = mydb[document]
            mydoc = mycol.find(query)
            return pd.DataFrame(list(mydoc))
        except Exception as ex:
            print(ex)
            return None

    def clear(self, db, document):
        try:
            client = self.getConnection(True)
            mydb = client[db]
            mycol = mydb[document]
            result = mycol.remove()
            return result
        except Exception as ex:
            print(ex)
            return None

    def insertMany(self, db, document, array):
        try:
            client = self.getConnection(True)
            mydb = client[db]
            mycol = mydb[document]
            result = mycol.insert_many(array)
            return result
        except Exception as ex:
            print(ex)
            return None