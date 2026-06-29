import pandas as pd

df = pd.read_csv("data/proccessed/customer_clusters.csv")

print(df["Cluster"].value_counts())

print(df.groupby("Cluster").mean())