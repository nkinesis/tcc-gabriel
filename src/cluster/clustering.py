import numpy as np
from numpy import unique
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans

def doKmeans(df, num_clusters):
    model = KMeans(n_clusters=num_clusters)
    model.fit(df)
    yhat = model.predict(df)
    clusters = unique(yhat)
    return {
        "yhat": yhat,
        "clusters": clusters
    }