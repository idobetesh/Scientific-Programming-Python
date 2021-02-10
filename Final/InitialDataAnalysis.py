import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split

df = pd.read_csv('./Data/customers2.csv')
df = df.drop(['ID'], axis=1)
print(f"Male count: {sum(df['Gender'] == 'Male')}")
print(f"Female count: {sum(df['Gender'] == 'Female')}")

# ['Healthcare' 'Engineer' 'Lawyer' 'Entertainment' 'Artist' 'Executive' 'Doctor' 'Homemaker' 'Marketing' nan]
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

# drop all rows where 'Profession' is Na

# Numinal categorical features => Profession | Graduated | Ever_Married | Gender
# Ordinal categorical features => Spending_Score | Group

# Replace all 'na' with median [numeric only]
# Integer replacment
df.Age = df.Age.fillna(df.Age.median())
df.Work_Experience = df.Work_Experience.fillna(df.Work_Experience.median())
df.Family_Size = df.Family_Size.fillna(df.Family_Size.median())
df.Shop_Day = df.Shop_Day.fillna(df.Shop_Day.median())
df.Shop_Other.fillna(df.Shop_Other.median())
df.Shop_Dairy.fillna(df.Shop_Dairy.median())
df.Shop_Household.fillna(df.Shop_Household.median())
df.Shop_Meat.fillna(df.Shop_Meat.median())
# Keep all float numbers 3 digits rounded
df = df.round(3)

# Keep all categorical data in lower case
df.Spending_Score = df.Spending_Score.str.lower()

# Lastly, drop all Categorical 'na'
df = df.dropna()

# df.to_csv('Data/clean_customers.csv')
# df['Profession'].hist(color='orange', bins=len(df['Profession'].unique()), edgecolor='blue')
# plt.title('Profession Distribution on Clean Data')
# plt.ylabel('Count', color='blue')
# plt.xlabel('Profession', color='blue')
# plt.tight_layout()
# plt.grid(True)
# plt.show()

df['Gender'].hist(bins=len(df['Gender'].unique()), edgecolor='orange')
plt.title('Gender Distribution on Clean Data')
plt.ylabel('Count', color='blue')
plt.xlabel('Gender', color='blue')
plt.tight_layout()
plt.grid(True) 
plt.show()

print(f"Healthcare count: {sum(df['Profession'] == 'Healthcare')}")
print(f"Engineer count: {sum(df['Profession'] == 'Engineer')}")
print(f"Lawyer count: {sum(df['Profession'] == 'Lawyer')}")
print(f"Entertainment count: {sum(df['Profession'] == 'Entertainment')}")
print(f"Artist count: {sum(df['Profession'] == 'Artist')}")
print(f"Executive count: {sum(df['Profession'] == 'Executive')}")
print(f"Doctor count: {sum(df['Profession'] == 'Doctor')}")
print(f"Homemaker count: {sum(df['Profession'] == 'Homemaker')}")
print(f"Marketing count: {sum(df['Profession'] == 'Marketing')}")