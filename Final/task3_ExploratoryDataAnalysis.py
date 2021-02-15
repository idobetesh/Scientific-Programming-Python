import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

# df = pd.read_csv('./Data/clean_customers.csv')
df = pd.read_csv('./Data/clean_customers2.csv')

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

# age = pd.cut(df['Age'], [18,25,40,60,100])
# pd.set_option('display.max_rows', None, 'display.max_columns', None)
# print(df.pivot_table('Avg_Shop', [age, 'Group', 'Spending_Score']))


# df['Animal_Product_Avg'] = (df['Shop_Dairy'] + df['Shop_Meat']) / 2
# pd.set_option('display.max_rows', None, 'display.max_columns', None)
# print(df.pivot_table('Shop_Meat', ['Group']))
# print(df.pivot_table('Shop_Dairy', ['Group']))
# print(df.pivot_table('Ever_Married', ['Group']))

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

# df = pd.concat([df, pd.get_dummies(df["Gender"], prefix="Gender")], axis=1)
# df = pd.concat([df, pd.get_dummies(df["Ever_Married"], prefix="Ever_Married")], axis=1)
# df = pd.concat([df, pd.get_dummies(df["Graduated"], prefix="Graduated")], axis=1)
# df = pd.concat([df, pd.get_dummies(df["Profession"], prefix="Profession")], axis=1)
# df["Age_Range"] = np.where(df.Age>=60, "60+", np.where(df.Age>=50, "50-60", np.where(df.Age>=40, "40-50", np.where(df.Age>=30, "30-40", np.where(df.Age>=18, "18-30", "18-")))))
# df["Work_Experience_Range"] = np.where(df.Work_Experience>=10, "10+", np.where(df.Work_Experience>=5, "5-10", "0-5"))
# df["Family_Size_Range"] = np.where(df.Family_Size>=6, "6+", np.where(df.Family_Size>=3, "3-6", "0-3"))



print(df.groupby(['Profession', 'Gender'])['Spending_Score'].aggregate('mean').unstack())


# df['Shop_Day'].hist(bins=len(df['Shop_Day'].unique()), edgecolor='orange')
# plt.title('Shop_Day Distribution')
# plt.ylabel('Count', color='blue')
# plt.xlabel('Shop_Day', color='blue')
# plt.tight_layout()
# plt.grid(True) 
# plt.show()


# sns.violinplot(data=df["Age"], color='yellow')
# plt.show()
# sns.displot(data=df['Work_Experience'], kde=True)
# plt.show()
# sns.displot(data=df['Family_Size'], kde=True, color='green')
# plt.show()

# fig, axarr = plt.subplots(3, 3, figsize=(30, 18))
# sns.countplot(x="Gender", hue = "Group", data = df, ax=axarr[0][0])
# sns.countplot(x="Ever_Married", hue = "Group", data = df, ax=axarr[0][1])
# sns.countplot(x="Graduated", hue = "Group", data = df, ax=axarr[0][2])
# sns.countplot(x="Profession", hue = "Group", data = df, ax=axarr[1][0])
# sns.countplot(x="Spending_Score", hue = "Group", data = df, ax=axarr[1][1])
# sns.countplot(x="Age_Range", hue = "Group", data = df, ax=axarr[2][0])
# sns.countplot(x="Work_Experience_Range", hue = "Group", data = df, ax=axarr[2][1])
# plt.show()

####################### CORR ####################### 
# corr = df_oh.corr()
# mask = np.triu(np.ones_like(corr, dtype=bool))
# f, ax = plt.subplots(figsize=(8,6))
# cmap = sns.diverging_palette(200,10,as_cmap=True)
# sns.heatmap(corr, annot=True, mask=mask, cmap=cmap, center=0, square=True, linewidths=5)
# plt.show()
