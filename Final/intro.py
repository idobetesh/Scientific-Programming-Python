import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

df = pd.read_csv('./Data/customers2.csv')
df = df.drop(['ID'], axis=1)
print(df['Profession'].unique())
print(f"Male count: {sum(df['Gender'] == 'Male')}")
print(f"Female count: {sum(df['Gender'] == 'Female')}")
print(df.describe())
print(df.info())