import numpy as np
from numpy import unique
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans

class Clustering:
    def __init__(self, num_clusters):
        self.num_clusters = num_clusters if num_clusters else 1
        
    def doKmeans(self, df):
        model = KMeans(n_clusters=self.num_clusters)
        model.fit(df)
        yhat = model.predict(df)
        clusters = unique(yhat)
        return {
            "yhat": yhat,
            "clusters": clusters
        }