import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/raw/Amazon.csv")

sns.countplot(x="Gender", data=df)

plt.title("Gender Distribution")
plt.savefig("outputs/gender_distribution.png")
plt.close()