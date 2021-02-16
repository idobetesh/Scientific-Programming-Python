import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

# df = pd.read_csv('../Data/customers2.csv')
df = pd.read_csv('../Data/avg_new.csv')

# ax1 = sns.scatterplot(data=df, x='Avg_Shop',y='Age', hue='Group')
# ax2 = sns.scatterplot(data=df, x='Shop_Household',y='Work_Experience', hue='Group')
# ax3 = sns.scatterplot(data=df, x='Shop_Meat',y='Age', hue='Group', y_bins=[20,30,40,60,80])


# ax4 = sns.pairplot(data=df, hue='Group', hue_order=['A','B','C','D'],
# x_vars=['Shop_Meat','Shop_Dairy','Shop_Household','Shop_Other'], 
# y_vars=['Shop_Meat','Shop_Dairy','Shop_Household','Shop_Other']) 


# ax4 = sns.pairplot(data=df, hue='Group', hue_order=['A','B','C','D'],
#       vars=['Shop_Meat','Shop_Dairy','Shop_Household','Shop_Other'])
# ax4.savefig('../Data/All-Shop-Pair-Plot.pdf')

# ax5 = sns.pairplot(data=df, hue='Group', hue_order=['A','B','C','D'],
# vars=['Age','Family_Size','Work_Experience','Shop_Day'])
# ax5.savefig('../Data/ax5.pdf')

g = sns.catplot(x="Avg_Shop_Range", y="Age", hue="Group", hue_order=['A','B','C','D'], data=df, kind="violin")

g.savefig('../Attachments/Avg_Shop_Range-Age-Catplot.pdf')
plt.show()