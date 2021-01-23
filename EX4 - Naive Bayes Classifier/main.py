import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

penguins = pd.read_csv('./Data/penguins.csv')
target = penguins.species

# Category -> Numeric
penguins['species'] = pd.Categorical(penguins.species, ordered=False, categories=['Adelie','Chinstrap','Gentoo']).codes+1
penguins['island'] = pd.Categorical(penguins.island, ordered=False, categories=['Torgersen','Biscoe','Gentoo','Dream']).codes+1
penguins['sex'] = pd.get_dummies(penguins['sex'])

# remove NaN
penguins.bill_length_mm = penguins.bill_length_mm.fillna(penguins.bill_length_mm.mean())
penguins.bill_depth_mm = penguins.bill_depth_mm.fillna(penguins.bill_depth_mm.mean())
penguins.flipper_length_mm = penguins.flipper_length_mm.fillna(penguins.flipper_length_mm.mean())
penguins.body_mass_g = penguins.body_mass_g.fillna(penguins.body_mass_g.mean())

penguins = penguins.drop('species', axis='columns')
print(penguins.tail(10))


'''check 2 most accurate features [?]'''
# corr = penguins.corr()
# sb.heatmap(corr, vmin=-1, annot=True, cmap='coolwarm')
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(penguins, target, train_size=0.8)

print(f'train set size: {len(X_train)} \ntest set size:{len(X_test)}')

model = GaussianNB()
model.fit(X_train, y_train)
print(f'score: {model.score(X_test, y_test)}')

print(f'test[y]:\n{y_test[:10]}')
print(f'predict: {model.predict(X_test[:10])}')
