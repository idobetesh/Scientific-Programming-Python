import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

df = pd.read_csv('./Data/customers2.csv')
df = df.drop(['ID'], axis=1)
print(df['Profession'].unique())
print(f"Male count: {sum(df['Gender'] == 'Male')}")
print(f"Female count: {sum(df['Gender'] == 'Female')}")
print(df.describe())
print(df.info())

# ['Healthcare' 'Engineer' 'Lawyer' 'Entertainment' 'Artist' 'Executive''Doctor' 'Homemaker' 'Marketing' nan]
def printProfessionCount(df):
    print(f"Healthcare count: {sum(df['Profession'] == 'Healthcare')}")
    print(f"Engineer count: {sum(df['Profession'] == 'Engineer')}")
    print(f"Lawyer count: {sum(df['Profession'] == 'Lawyer')}")
    print(f"Entertainment count: {sum(df['Profession'] == 'Entertainment')}")
    print(f"Artist count: {sum(df['Profession'] == 'Artist')}")
    print(f"Executive count: {sum(df['Profession'] == 'Executive')}")
    print(f"Doctor count: {sum(df['Profession'] == 'Doctor')}")
    print(f"Homemaker count: {sum(df['Profession'] == 'Homemaker')}")
    print(f"Marketing count: {sum(df['Profession'] == 'Marketing')}")
    print("==============================================================")

printProfessionCount(df)
# drop all rows where 'Profession' is Na
df = df.dropna(axis=0, subset=['Profession'])

# df['Profession'].hist(color='orange', bins=len(df['Profession'].unique()), edgecolor='blue')
# plt.title('Profession Distribution')
# plt.ylabel('Count', color='blue')
# plt.xlabel('Profession', color='blue')
# plt.tight_layout()
# plt.grid(True)
# plt.show()
print(f"Male count: {sum(df['Gender'] == 'Male')}")
print(f"Female count: {sum(df['Gender'] == 'Female')}")
df['Gender'].hist(bins=len(df['Gender'].unique()), edgecolor='orange')
plt.title('Gender Distribution')
plt.ylabel('Count', color='blue')
plt.xlabel('Gender', color='blue')
plt.tight_layout()
plt.grid(True) 
plt.show()

printProfessionCount(df)