import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

penguins = pd.read_csv('../Data/penguins.csv')
# target = penguins.species
df = penguins.copy()
target = df.species

# remove NaN
df.bill_length_mm = df.bill_length_mm.fillna(df.bill_length_mm.median())
df.bill_depth_mm = df.bill_depth_mm.fillna(df.bill_depth_mm.median())
df.flipper_length_mm = df.flipper_length_mm.fillna(df.flipper_length_mm.median())
df.body_mass_g = df.body_mass_g.fillna(df.body_mass_g.median())
df = df.dropna()

# 1.1 Two most accurate features are bill_depth_mm and bill_length_mm according to their distribution on the plot below
sb.pairplot(df, hue='species')
plt.show()

# Category -> Numeric
df['species'] = pd.Categorical(df.species, ordered=True, categories=['Adelie','Chinstrap','Gentoo']).codes+1
df['island'] = pd.Categorical(df.island, ordered=True, categories=['Torgersen','Biscoe','Dream']).codes+1
df['sex'] = pd.Categorical(df.sex, ordered=True, categories=['Male','Female']).codes+1

# 1.2 Predict using Naive Bayes 
X_axis = df[['bill_depth_mm', 'bill_length_mm']]
y_axis = df['species']

X_train, X_test, y_train, y_test = train_test_split(X_axis ,y_axis, train_size=0.8)
model = GaussianNB()                 
model.fit(X_train, y_train)              

y_model = model.predict(X_test)  
print(f'Prediction score: {model.score(X_test, y_test)*100}%')

# 1.3 Filled contour plot:

