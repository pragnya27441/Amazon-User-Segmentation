import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data/proccessed/cleaned_data.csv")

le = LabelEncoder()

for column in df.columns:
    if df[column].dtype !="int64":
        df[column] = le.fit_transform(df[column])

print(df.head())

df.to_csv("data/proccessed/encoded_data.csv", index=False)

print("Encoding completed successfully!")