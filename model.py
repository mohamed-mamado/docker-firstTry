import pandas as pd
from sklearn.cluster import KMeans


def clustering(df):

    # Implement the K-means algorithm
    # You should choose suitable columns for K-means


    df = df[['release_year', 'duration']]
    kmeans = KMeans(n_clusters=5).fit(df)

    # Save the number of records in each cluster
    cluster_sizes = pd.Series(kmeans.labels_).value_counts().to_frame()
    cluster_sizes.to_csv("/home/doc-bd-a1/k.txt")
    