import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

df = pd.read_csv('../Data/penguins.csv')

# Remove NaN
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
X_axis = df[['bill_length_mm', 'bill_depth_mm']]
y_axis = df['species']

X_train, X_test, y_train, y_test = train_test_split(X_axis ,y_axis, train_size=0.8)
model = GaussianNB()                 
model.fit(X_train, y_train)              

y_model = model.predict(X_test)  
print(f'Prediction score: {model.score(X_test, y_test)*100}%')

# 1.3 Filled contour plot:
species_dict = {1: 'Adelie', 2: 'Chinstrap', 3: 'Gentoo'}
col_list = df.columns

x_min, x_max = X_train.loc[:, 'bill_length_mm'].min()-1, X_train.loc[:, 'bill_length_mm'].max()+1
y_min, y_max = X_train.loc[:, 'bill_depth_mm'].min()-1, X_train.loc[:, 'bill_depth_mm'].max()+1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.2), np.arange(y_min, y_max, 0.2))

Z = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])
Z = np.argmax(Z, axis=1)
Z = Z.reshape(xx.shape)

if len(model.classes_) == 3:
    plt.contourf(xx, yy, Z)
    plt.clim(0, 6)
    plt.colorbar()
else:
    plt.contourf(xx, yy, Z)
    plt.clim(0, 6)
    plt.colorbar()

fig = plt.gcf()
predictions = model.predict(X_axis)

# 1.4
# Wrong predicted
wrongs = []
sp_i = 0
for i, col in enumerate(col_list):
    if col == 'species':
        sp_i = i
        break

val_t = df.values.tolist()
for i in range(len(df)):
    if predictions[i] != val_t[i][sp_i]:
        _t = val_t[i]
        _t[0] = species_dict[_t[0]]
        wrongs.append(val_t[i])

wrongs = pd.DataFrame(wrongs, columns=col_list)
sp = ['Adelie','Chinstrap','Gentoo','',''] 

sb.scatterplot(data=wrongs, x='bill_length_mm', y='bill_depth_mm', hue='species', hue_order=sp)
plt.show()

# 1.5 Classification report
print(metrics.classification_report(y_test, y_model))