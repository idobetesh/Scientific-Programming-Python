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


df = pd.read_csv('../Data/clean_customers2.csv')
# df = pd.read_csv('../Data/avg_new.csv')

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

############################ GNB simple example ############################
X_customers = df[['Age','Shop_Other','Shop_Dairy','Shop_Household','Shop_Meat','Family_Size']].copy()
print(X_customers)
y_customers = df['Group']

X_train, X_test, y_train, y_test = train_test_split(X_customers,y_customers,train_size=0.7,random_state=1)

model = GaussianNB()
model.fit(X_train,y_train)

y_model = model.predict(X_test)
y_pred = pd.Series(y_model,name="prediction")
predicted = pd.concat([X_test.reset_index(),y_test.reset_index(),y_pred],axis=1)
print(predicted)
print(f"accuracy_score: {round(metrics.accuracy_score(y_test, y_model)*100, 3)}%")

############################ end example ############################




def bayes_plot(df,model="gnb",spread=80):
    df.dropna()
    colors = 'seismic'
    col1 = df.columns[0]
    col2 = df.columns[1]
    target = df.columns[2]
    sns.scatterplot(data=df, x=col1, y=col2, hue=target)
    plt.show()
    y = df[target]  # Target variable
    X = df.drop(target, axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=1)  # 80% training and 20% test

    clf = GaussianNB()
    if (model != "gnb"):
        clf = DecisionTreeClassifier(max_depth=model)
    clf = clf.fit(X_train, y_train)

    # Train Classifer
    prob = len(clf.classes_) == 2

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)
    print(metrics.classification_report(y_test, y_pred))
    hueorder = clf.classes_
    def numify(val):
        return np.where(clf.classes_ == val)[0]

    Y = y.apply(numify)
    x_min, x_max = X.loc[:, col1].min() - 1, X.loc[:, col1].max() + 1
    y_min, y_max = X.loc[:, col2].min() - 1, X.loc[:, col2].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.2))

    Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])
    if prob:
        Z = Z[:,1]-Z[:,0]
    else:
        colors = "Set1"
        Z = np.argmax(Z, axis=1)

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=colors, alpha=0.5)
    plt.colorbar()
    if not prob:
        plt.clim(0,len(clf.classes_)+3)
    sns.scatterplot(data=df[::spread], x=col1, y=col2, hue=target, hue_order=hueorder,palette=colors)
    fig = plt.gcf()
    fig.set_size_inches(12, 8)
    plt.show()



print(y_customers)
# X_customers2 = df[['Age','Shop_Other']].copy()
X_customers2 = df[['Age','Shop_Other']].copy()
bayes_plot(pd.concat([X_customers2,y_customers],axis=1),spread = 1)
