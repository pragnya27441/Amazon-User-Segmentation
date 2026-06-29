import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/raw/Amazon.csv")

sns.countplot(x="Purchase_Frequency", data=df)

plt.title("Purchase Frequency")
plt.xticks(rotation=45)
plt.savefig("outputs/purchase_frequency.png")
plt.close()