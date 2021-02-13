import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

df = pd.read_csv('./Data/clean_customers.csv')

# x_vars=['Shop_Other','Shop_Dairy','Shop_Household','Shop_Meat'], y_vars=['Age', 'Work_Experience'], 
# sns.pairplot(df, hue='Group', hue_order=['A','B','C','D'], height=1)
# plt.show()

# df['Avg_Shop'] = (df['Shop_Other'] + df['Shop_Dairy'] + df['Shop_Household'] + df['Shop_Meat']) / 4
# df = df.round(3)

# x_vars=['Shop_Other','Shop_Dairy','Shop_Household','Shop_Meat'], y_vars=['Avg_Shop'], 
# sns.pairplot(df, hue='Group', hue_order=['A','B','C','D'], x_vars=['Shop_Other','Shop_Dairy','Shop_Household','Shop_Meat'], y_vars=['Avg_Shop'], kind='reg')
# plt.show()

# df['Spending_Score'] = pd.Categorical(df.Spending_Score, ordered=True, categories=['high', 'average','low']).codes+1
# df['Group'] = pd.Categorical(df.Group, ordered=True, categories=['A','B','C','D']).codes+1
age = pd.cut(df['Age'], [0,25,40,60,100])
# print(df.pivot_table('Shop_Day', ['Gender', age]))

corr = df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
f, ax = plt.subplots(figsize=(8,6))
cmap = sns.diverging_palette(200,10,as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, center=0, square=True, linewidths=5)
plt.show()

# print(df.groupby(['Profession', 'Gender'])['Spending_Score'].aggregate('mean').unstack())


# df['Shop_Day'].hist(bins=len(df['Shop_Day'].unique()), edgecolor='orange')
# plt.title('Shop_Day Distribution')
# plt.ylabel('Count', color='blue')
# plt.xlabel('Shop_Day', color='blue')
# plt.tight_layout()
# plt.grid(True) 
# plt.show()
