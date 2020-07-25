from pymongo import MongoClient
import pandas as pd
import numpy as np

def getConnection(type):
    try:
        connStr = "mongodb://localhost:27017"
        client = MongoClient(connStr)
        db = client.admin
        status = db.command("serverStatus")
        if not type or type == "test":
            return status
        else:
            return client
    except Exception as ex:
        print(ex)
        return None

def doQuery(db, document, query):
    try:
        client = getConnection(True)
        mydb = client[db]
        mycol = mydb[document]
        mydoc = mycol.find(query)
        return pd.DataFrame(list(mydoc))
    except Exception as ex:
        print(ex)
        return None

def insertMany(db, document, array):
    try:
        client = getConnection(True)
        mydb = client[db]
        mycol = mydb[document]
        result = mycol.insert_many(array)
        return result
    except Exception as ex:
        print(ex)
        return None