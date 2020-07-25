import pandas as pd
import numpy as np

def createDf(list):
    return pd.DataFrame(list)

def deleteCol(df, colName):
    del df[colName]
    return True

def convertDf(df, type):
    df.astype(type)
    return True

def toJson(df):
    return df.to_dict(orient='records')

