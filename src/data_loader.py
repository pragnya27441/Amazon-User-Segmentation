import pandas as pd


df = pd.read_csv("data/raw/Amazon.csv")


print("\n========== FIRST 5 ROWS ==========\n")
print(df.head())


print("\n========== SHAPE ==========\n")
print(df.shape)


print("\n========== COLUMNS ==========\n")
print(df.columns)


print("\n========== INFO ==========\n")
df.info()

print("\n========== STATISTICS ==========\n")
print(df.describe())

print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())