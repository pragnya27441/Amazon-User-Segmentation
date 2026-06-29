import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("data/proccessed/scaled_data.csv")

kmeans = KMeans(n_clusters=4, random_state=42)

kmeans.fit(df)

df["Cluster"] = kmeans.labels_

print(df.head())

df.to_csv("data/proccessed/customer_clusters.csv", index=False)

print("Customer Segmentation Completed!")