import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

df = pd.read_csv('../Data/clean_customers2.csv')
# df = pd.read_csv('../Data/avg.csv')
# df = pd.read_csv('./Data/clean_customers2.csv')
# print(df)

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

# age = pd.cut(df['Age'], [18,30,40,50,60,100])
# pd.set_option('display.max_rows', None, 'display.max_columns', None)
# print(df.pivot_table('Avg_Shop', [age, 'Group', 'Gender']))


# df['Animal_Product_Avg'] = (df['Shop_Dairy'] + df['Shop_Meat']) / 2
# pd.set_option('display.max_rows', None, 'display.max_columns', None)
# print(df.pivot_table('Shop_Meat', ['Group']))
# print(df.pivot_table('Shop_Dairy', ['Group']))
# print(df.pivot_table('Animal_Product_Avg', ['Group']))

# df = pd.concat([df, pd.get_dummies(df['Gender'], prefix='Gender')], axis=1)
# df = pd.concat([df, pd.get_dummies(df['Ever_Married'], prefix='Ever_Married')], axis=1)
# df = pd.concat([df, pd.get_dummies(df['Graduated'], prefix='Graduated')], axis=1)
# df = pd.concat([df, pd.get_dummies(df['Profession'], prefix='Profession')], axis=1)
# df['Age_Range'] = np.where(df.Age>=60, '60+', np.where(df.Age>=50, '50-60', np.where(df.Age>=40, '40-50', np.where(df.Age>=30, '30-40', np.where(df.Age>=18, '18-30', '-18')))))
# df['Work_Experience_Range'] = np.where(df.Work_Experience>=10, '10+', np.where(df.Work_Experience>=5, '5-10', '0-5'))
# df['Family_Size_Range'] = np.where(df.Family_Size>=6, '6+', np.where(df.Family_Size>=3, '3-6', '0-3'))
# df['Shop_Other_Range'] = np.where(df.Shop_Other>=20, '20+', np.where(df.Shop_Other>=10, '10-20', np.where(df.Shop_Other>=0, '0-10', '-0'))) # -10,0,10,20
# df['Shop_Dairy_Range'] = np.where(df.Shop_Dairy>=20, '20+', np.where(df.Shop_Dairy>=10, '10-20', np.where(df.Shop_Dairy>=0, '0-10', '-0'))) # -10,0,10,20
# df['Shop_Household_Range'] = np.where(df.Shop_Household>=20, '20+', np.where(df.Shop_Household>=10, '10-20', np.where(df.Shop_Household>=0, '0-10', '-0'))) # -10,0,10,20
# df['Shop_Meat_Range'] = np.where(df.Shop_Meat>=20, '20+', np.where(df.Shop_Meat>=10, '10-20', np.where(df.Shop_Meat>=0, '0-10', '-0'))) # -10,0,10,20
# df['Spending_Score_Level'] = pd.Categorical(df['Spending_Score'], ordered=True, categories=['low', 'average', 'high']).codes+1 
# df['Group_Level'] = pd.Categorical(df['Group'], ordered=True, categories=['A','B','C','D']).codes+1 
# df.to_csv('Data/clean_customers2.csv', index=False)


# df['Shop_Day'].hist(bins=len(df['Shop_Day'].unique()), edgecolor='orange')
# plt.title('Shop_Day Distribution')
# plt.ylabel('Count', color='blue')
# plt.xlabel('Shop_Day', color='blue')
# plt.tight_layout()
# plt.grid(True) 
# plt.show()


# sns.violinplot(data=df['Age'], color='yellow')
# plt.show()
# sns.displot(data=df['Work_Experience'], kde=True)
# plt.show()
# sns.displot(data=df['Family_Size'], kde=True, color='green')
# plt.show()


####################### COUNTPLOTS ####################### 
# fig, ax = plt.subplots(6, 2, figsize=(20, 35))
# group_order = ['A','B','C','D']
# sns.countplot(x='Gender', hue='Group', data=df, ax=ax[0][0], hue_order=group_order, palette='husl')
# sns.countplot(x='Age_Range', hue='Group', data=df, ax=ax[0][1], hue_order=group_order, palette='husl')
# sns.countplot(x='Profession', hue='Group', data=df, ax=ax[1][0], hue_order=group_order, palette='husl')
# sns.countplot(x='Spending_Score', hue='Group', data=df, ax=ax[1][1], hue_order=group_order, palette='husl')
# sns.countplot(x='Ever_Married', hue='Group', data=df, ax=ax[2][0], hue_order=group_order, palette='husl')
# sns.countplot(x='Graduated', hue='Group', data=df, ax=ax[2][1], hue_order=group_order, palette='husl')
# sns.countplot(x='Work_Experience_Range', hue='Group', data=df, ax=ax[3][0], hue_order=group_order, palette='husl')
# sns.countplot(x='Family_Size_Range', hue='Group', data=df, ax=ax[3][1], hue_order=group_order, palette='husl')
# sns.countplot(x='Shop_Meat_Range', hue='Group', data=df, ax=ax[4][0], hue_order=group_order, palette='husl')
# sns.countplot(x='Shop_Dairy_Range', hue='Group', data=df, ax=ax[4][1], hue_order=group_order, palette='husl')
# sns.countplot(x='Shop_Other_Range', hue='Group', data=df, ax=ax[5][0], hue_order=group_order, palette='husl')
# sns.countplot(x='Shop_Household_Range', hue='Group', data=df, ax=ax[5][1], hue_order=group_order, palette='husl')
# plt.show()	

####################### CORR ####################### 
# df['Avg_Shop_Range'] = np.where(df.Avg_Shop>=15, '15+', np.where(df.Avg_Shop>=5, '5-15', '-5')) # -3,5,15,
# ax10 = df.groupby(['Avg_Shop_Range'])['Group'].value_counts().unstack()
# print(ax10)
# ax10.plot(kind='bar', figsize = (20,35))
# plt.show()
# df.to_csv('../Data/avg_new.csv', index=False)



# corr = df.corr()
# fig, ax = plt.subplots(1, figsize=(25,25))
# sns.heatmap(corr, annot=True, fmt=',.2f')
# plt.title('Correlation Map', fontsize=20)
# plt.show()



# ax1 = df.groupby(['Ever_Married'])['Age_Range'].value_counts().unstack()
# ax2 = df.groupby(['Age_Range'])['Profession'].value_counts().unstack()
# ax3 = df.groupby(['Ever_Married'])['Spending_Score'].value_counts().unstack()
# ax4 = df.groupby(['Age_Range'])['Spending_Score'].value_counts().unstack()
# ax5 = df.groupby(['Spending_Score'])['Profession'].value_counts().unstack()
# ax6 = df.groupby(['Gender'])['Profession'].value_counts().unstack()
# ax7 = df.groupby(['Graduated'])['Profession'].value_counts().unstack()
# ax8 = df.groupby(['Ever_Married'])['Profession'].value_counts().unstack()
# ax9 = df.groupby(['Age_Range'])['Group'].value_counts().unstack()


#count plot
# fig, ax = plt.subplots(4,2)
# ax1.plot(kind='bar',ax=ax[0][0],figsize = (20,35))
# ax[0][0].set_title(str(ax1))

# ax2.plot(kind='bar',ax=ax[0][1],figsize = (20,35))
# ax[0][1].set_title(str(ax2))

# ax3.plot(kind='bar',ax=ax[1][0],figsize = (20,35))
# ax[1][0].set_title(str(ax3))

# ax4.plot(kind='bar',ax=ax[1][1],figsize = (20,35))
# ax[1][1].set_title(str(ax4))

# ax5.plot(kind='bar',ax=ax[2][0],figsize = (20,35))
# ax[2][0].set_title(str(ax5))

# ax6.plot(kind='bar',ax=ax[2][1],figsize = (20,35))
# ax[2][1].set_title(str(ax6))

# ax7.plot(kind='bar',ax=ax[3][0],figsize = (20,35))
# ax[3][0].set_title(str(ax7))

# ax8.plot(kind='bar',ax=ax[3][1],figsize = (20,35))
# ax[3][1].set_title(str(ax7))
# plt.show()

##############################################################
# fig, ax = plt.subplots(8,1)
# ax1.plot(kind='bar',ax=ax[0],figsize = (20,35))
# ax[0].set_title(str(ax1))

# ax2.plot(kind='bar',ax=ax[0],figsize = (20,35))
# ax[0].set_title(str(ax2))

# ax3.plot(kind='bar',ax=ax[1],figsize = (20,35))
# ax[1].set_title(str(ax3))

# ax4.plot(kind='bar',ax=ax[2],figsize = (20,35))
# ax[2].set_title(str(ax4))

# ax5.plot(kind='bar',ax=ax[3],figsize = (20,35))
# ax[3].set_title(str(ax5))

# ax6.plot(kind='bar',ax=ax[4],figsize = (20,35))
# ax[5].set_title(str(ax6))

# ax7.plot(kind='bar',ax=ax[7],figsize = (20,35))
# ax[6].set_title(str(ax7))

# ax8.plot(kind='bar',ax=ax[8],figsize = (20,35))
# ax[8].set_title(str(ax7))
# plt.show()


fig, ax = plt.subplots(6, 2, figsize=(10, 10))
group_order = ['A','B','C','D']
sns.countplot(x='Gender', hue='Group', data=df, ax=ax[0][0], hue_order=group_order, palette='husl')
sns.countplot(x='Age_Range', hue='Group', data=df, ax=ax[0][1], hue_order=group_order, palette='husl')
sns.countplot(x='Profession', hue='Group', data=df, ax=ax[1][0], hue_order=group_order, palette='husl')
sns.countplot(x='Spending_Score', hue='Group', data=df, ax=ax[1][1], hue_order=group_order, palette='husl')
sns.countplot(x='Ever_Married', hue='Group', data=df, ax=ax[2][0], hue_order=group_order, palette='husl')
sns.countplot(x='Graduated', hue='Group', data=df, ax=ax[2][1], hue_order=group_order, palette='husl')
sns.countplot(x='Work_Experience_Range', hue='Group', data=df, ax=ax[3][0], hue_order=group_order, palette='husl')
sns.countplot(x='Family_Size_Range', hue='Group', data=df, ax=ax[3][1], hue_order=group_order, palette='husl')
sns.countplot(x='Shop_Meat_Range', hue='Group', data=df, ax=ax[4][0], hue_order=group_order, palette='husl')
sns.countplot(x='Shop_Dairy_Range', hue='Group', data=df, ax=ax[4][1], hue_order=group_order, palette='husl')
sns.countplot(x='Shop_Other_Range', hue='Group', data=df, ax=ax[5][0], hue_order=group_order, palette='husl')
sns.countplot(x='Shop_Household_Range', hue='Group', data=df, ax=ax[5][1], hue_order=group_order, palette='husl')
plt.show()

# ax9 = df.groupby(['Shop_Household_Range'])['Profession'].value_counts().unstack()

# table = pd.pivot_table(df, index=['Shop_Household_Range', 'Shop_Other_Range', 'Shop_Dairy_Range', 'Shop_Meat_Range'], aggfunc=np.mean)
# print(table)
# sns.pairplot(df, hue='Group', hue_order=['A','B','C','D'], kind='kde', x_vars=['Shop_Day', 'Family_Size'], y_vars=['Spending_Score_Level','Group_Level'])

