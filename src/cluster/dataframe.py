import pandas as pd
import numpy as np

def createDf(list):
    return pd.DataFrame(list)

def addCol(df, colName, colValues):
    df[colName] = colValues
    return df

def deleteCol(df, colName):
    del df[colName]
    return df

def convertDf(df, type):
    df = df.astype(type)
    return df

def toJson(df):
    return df.to_dict(orient='records')

