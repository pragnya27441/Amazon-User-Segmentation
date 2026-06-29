import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/raw/Amazon.csv")

sns.countplot(x="Customer_Reviews_Importance", data=df)

plt.title("Customer Reviews Importance")
plt.xticks(rotation=45)

plt.savefig("outputs/review_importance.png")
plt.close()