import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

# df = pd.read_csv('./Data/clean_customers.csv')
df = pd.read_csv('./Data/avg.csv')

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

# age = pd.cut(df['Age'], [0,25,40,60,100])
# pd.set_option('display.max_rows', None, 'display.max_columns', None)
# print(df.pivot_table('Avg_Shop', ['Gender', age, 'Group']))


pd.set_option('display.max_rows', None, 'display.max_columns', None)
print(df.pivot_table('Avg_Shop', ['Gender', age, 'Group']))



# COUNT_PRECENT_TABLE = pd.DataFrame()
# COUNT_PRECENT_TABLE["count"] = df["Group"].value_counts()
# COUNT_PRECENT_TABLE["count%"] = (df["Group"].value_counts()/df.shape[0])*100
# print(COUNT_PRECENT_TABLE)


# df_oh = pd.concat([df, pd.get_dummies(df['Gender'])], axis=1)
# df_oh = pd.concat([df_oh, pd.get_dummies(df['Group'])], axis=1)
# df_oh = pd.concat([df_oh, pd.get_dummies(df['Spending_Score'])], axis=1)
# df_oh = pd.concat([df_oh, pd.get_dummies(df['Profession'])], axis=1)
# df_oh = df_oh.drop(['Work_Experience'], axis=1)
# df_oh = df_oh.drop(['Shop_Day'], axis=1)
# df_oh = df_oh.drop(['Shop_Other'], axis=1)
# df_oh = df_oh.drop(['Family_Size'], axis=1)


# corr = df_oh.corr()
# mask = np.triu(np.ones_like(corr, dtype=bool))
# f, ax = plt.subplots(figsize=(8,6))
# cmap = sns.diverging_palette(200,10,as_cmap=True)
# sns.heatmap(corr, annot=True, mask=mask, cmap=cmap, center=0, square=True, linewidths=5)
# plt.show()

# print(df.groupby(['Profession', 'Gender'])['Spending_Score'].aggregate('mean').unstack())


# df['Shop_Day'].hist(bins=len(df['Shop_Day'].unique()), edgecolor='orange')
# plt.title('Shop_Day Distribution')
# plt.ylabel('Count', color='blue')
# plt.xlabel('Shop_Day', color='blue')
# plt.tight_layout()
# plt.grid(True) 
# plt.show()


count_precent_tablt_Shop_Day = pd.DataFrame()
count_precent_tablt_Shop_Day["count"] = df["Shop_Day"].value_counts()
count_precent_tablt_Shop_Day["count%"] = round((df["Shop_Day"].value_counts()/df.shape[0])*100, 3)
count_precent_tablt_Shop_Day
