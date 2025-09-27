import numpy as py
import pandas as pd
import matplotlib.pyplot as ptl
import seaborn as sns

df = pd.read_csv("Tips Dataset.csv")
df.head(10)
df.info()
df.describe()
df.columns
sns.pairplot(df)
sns.heatmap(df.corr(numeric_only=True), annot=True)