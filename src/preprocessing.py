import pandas as pd

df = pd.read_csv("data/raw/Amazon.csv")

df = df.dropna()

print("New Shape:", df.shape)

df.to_csv("data/proccessed/cleaned_data.csv",index=False)

print("Cleaned dataset saved successfully!")