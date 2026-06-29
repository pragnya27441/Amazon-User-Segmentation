import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/proccessed/encoded_data.csv")

df = df.drop("Timestamp", axis=1)

scaler = StandardScaler()

scaled_data = scaler.fit_transform(df)

scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

print(scaled_df.head())

scaled_df.to_csv("data/proccessed/scaled_data.csv", index=False)

print("Scaling completed successfully!")