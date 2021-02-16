import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn as skl
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
# import pydotplus


# df = pd.read_csv('../Data/customers2.csv')
df = pd.read_csv('../Data/avg_new.csv')
df['Avg_Shop'] = (df['Shop_Other'] + df['Shop_Dairy'] + df['Shop_Household'] + df['Shop_Meat']) / 4

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

# g = sns.catplot(x="Avg_Shop_Range", y="Age", hue="Group", hue_order=['A','B','C','D'], data=df, kind="violin")
# g.savefig('../Attachments/Avg_Shop_Range-Age-Catplot.pdf')

X_customers = df[['Age','Family_Size','Shop_Day','Shop_Other','Shop_Dairy','Shop_Household','Shop_Meat']].copy()
print(X_customers)
y_customers = df['Group']
print(y_customers)

X_train, X_test, y_train, y_test = train_test_split(X_customers,y_customers,train_size=0.8,random_state=1)
model = GaussianNB()
model.fit(X_train,y_train)
y_model = model.predict(X_test)
y_pred = pd.Series(y_model,name="prediction")
predicted = pd.concat([X_test.reset_index(),y_test.reset_index(),y_pred],axis=1)
print(predicted)
print(f"accuracy_score: {round(metrics.accuracy_score(y_test, y_model)*100, 3)}%")


