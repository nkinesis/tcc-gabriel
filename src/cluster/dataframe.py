import pandas as pd
import numpy as np

class Dataframe:

    def __init__(self, dftype):
        self.type = dftype if dftype else "pandas"

    def createDf(self, list):
        return pd.DataFrame(list)

    def addCol(self, df, colName, colValues):
        df[colName] = colValues
        return df

    def deleteCol(self, df, colName):
        del df[colName]
        return df

    def convertDf(self, df, type):
        df = df.astype(type)
        return df

    def toJson(self, df):
        return df.to_dict(orient='records')

