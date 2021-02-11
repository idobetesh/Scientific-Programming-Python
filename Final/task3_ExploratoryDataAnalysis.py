import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

df = pd.read_csv('./Data/avg.csv')

# x_vars=['Shop_Other','Shop_Dairy','Shop_Household','Shop_Meat'], y_vars=['Age', 'Work_Experience'], 
# sns.pairplot(df, hue='Group', hue_order=['A','B','C','D'], height=1)
# plt.show()

# df['Avg_Shop'] = (df['Shop_Other'] + df['Shop_Dairy'] + df['Shop_Household'] + df['Shop_Meat']) / 4
# df = df.round(3)

# x_vars=['Shop_Other','Shop_Dairy','Shop_Household','Shop_Meat'], y_vars=['Avg_Shop'], 
sns.pairplot(df, hue='Profession', x_vars=['Shop_Other','Shop_Dairy','Shop_Household','Shop_Meat'], y_vars=['Avg_Shop'], kind='reg')
plt.show()


# df['Shop_Day'].hist(bins=len(df['Shop_Day'].unique()), edgecolor='orange')
# plt.title('Shop_Day Distribution')
# plt.ylabel('Count', color='blue')
# plt.xlabel('Shop_Day', color='blue')
# plt.tight_layout()
# plt.grid(True) 
# plt.show()
