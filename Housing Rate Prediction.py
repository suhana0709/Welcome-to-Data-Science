import numpy as py
import pandas as pd
import matplotlib.pyplot as ptl
import seaborn as sns

df = pd.read_csv("USA_Housing.csv")
df.head(10)
df.info()
df.describe()
df.columns
sns.pairplot(df)
sns.heatmap(df.drop('Address', axis=1).corr(), annot=True)