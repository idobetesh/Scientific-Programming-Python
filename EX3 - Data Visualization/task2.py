import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

# ======================== Task 2 ======================== #

def task2():
    # load data from csv
    data = pd.read_csv("./Data/mobile_price_1.csv")
    # corr = data.corr()
    # print(corr)

    # 2.1
    #Correlation Heatmap Numerical values
    #mask = np.triu(np.ones_like(corr, dtype=bool))
    # f, ax = plt.subplots(figsize=(8, 6))
    # ax.set_title("Task2 - Correlation Heatmap Numerical values")
    # cmap = sb.diverging_palette(200, 10, as_cmap=True)
    # sb.heatmap(corr, mask=mask, cmap=cmap, center=0, square=True, linewidths=.5)
    # plt.show()

    # 2.2
    # Features correlated the most with the device price are:
    # 'battery_power', 'ram' and 'gen'.

    # 2.3
    # There are no other features correlated with the device price.

    # data_oh1 = pd.get_dummies(data['bluetooth'])
    # data_oh2 = pd.get_dummies(data["cores"])
    # data_oh3 = pd.get_dummies(data["speed"])
    # data_oh4 = pd.get_dummies(data["sim"])
    # data_oh5 = pd.get_dummies(data["screen"])
    # data_oh6 = pd.get_dummies(data["wifi"])
    # print(data_oh)

    # data_oh1 = pd.concat([data, pd.get_dummies(data['bluetooth'])],axis=1)
    # data_oh1 = pd.concat([data_oh1, pd.get_dummies(data['cores'])],axis=1)
    # data_oh1 = pd.concat([data_oh1, pd.get_dummies(data["sim"])],axis=1)
    # data_oh1 = pd.concat([data_oh1, pd.get_dummies(data['speed'])],axis=1)
    # data_oh1 = pd.concat([data_oh1, pd.get_dummies(data['screen'])],axis=1)
    # data_oh1 = pd.concat([data_oh1, pd.get_dummies(data['wifi'])],axis=1)
    # corr_oh = data_oh1.corr()
    # print(corr_oh)

    # Correlation Heatmap include Categorical values
    # mask = np.triu(np.ones_like(corr_oh, dtype=bool))
    # f, ax = plt.subplots(figsize=(8, 6))
    # ax.set_title("Task2 - Correlation Heatmap Categorical values")
    # cmap = sb.diverging_palette(200, 10, as_cmap=True)
    # sb.heatmap(corr_oh, mask=mask, cmap=cmap, center=0, square=True, linewidths=.5)
    # plt.show()

    # 2.4
    # price - battery_power relationship
    # plt.scatter(data.battery_power, data.price, alpha=0.5, marker='^', color='green')
    # plt.title('price - battery_power relationship'.format(data.battery_power, data.price))
    # plt.xlabel('battery_power')
    # plt.ylabel('price')
    # plt.show()

    # price - ram relationship
    # plt.scatter(data.ram, data.price, alpha=0.5, marker='^', color='green')
    # plt.title('price - ram relationship'.format(data.ram, data.price))
    # plt.xlabel('ram')
    # plt.ylabel('price')
    # plt.show()

    # price - gen relationship
    # plt.scatter(data.gen, data.price, alpha=0.5, marker='^', color='green')
    # plt.title('price - gen relationship')
    # plt.xlabel('gen')
    # plt.ylabel('price')
    # plt.show()


    # 2.5
    #pivot table
    battery_power = pd.qcut(data['battery_power'], 4)
    ram = pd.qcut(data['ram'], 4)
    gen = pd.cut(data['gen'], [2,3,4])
    print(data.pivot_table('price', [battery_power, ram, gen]))


if __name__ == "__main__":
    task2()
