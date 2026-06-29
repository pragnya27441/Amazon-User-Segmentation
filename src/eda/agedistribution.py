import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/raw/Amazon.csv")

sns.histplot(df["age"], bins=10)

plt.title("Age Distribution")
plt.savefig("outputs/age_distribution.png")
plt.close()