import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

# ======================== Task 2 ======================== #

def task2():
    # load data from csv
    data = pd.read_csv("./Data/mobile_price_1.csv")
    corr = data.corr()
    print(corr)
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 2.1
    f, ax = plt.subplots(figsize=(8, 6))
    ax.set_title("Task2 - Correlation Heatmap")
    cmap = sb.diverging_palette(200, 10, as_cmap=True)
    sb.heatmap(corr, mask=mask, cmap=cmap, center=0, square=True, linewidths=.5)
    # plt.show()

    # 2.2
    # Features correlated the most with the device price are:
    # 'battery_power', 'ram' and 'gen'.

    # 2.3
    data_oh = pd.get_dummies(data["bluetooth"])
    print(data_oh)



if __name__ == "__main__":
    task2()
