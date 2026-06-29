import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/raw/Amazon.csv")

sns.countplot(x="Purchase_Categories", data=df)

plt.title("Purchase Categories")
plt.xticks(rotation=90)

plt.savefig("outputs/product_category.png")
plt.close()