import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

# ======================== Task 4 ======================== #

def task4():
    # load data from csv
    data = pd.read_csv("./Data/mobile_price_1.csv")

    # 4.1
    # grid = sb.PairGrid(data, vars=['price', 'talk_time', 'battery_power', 'ram'])
    # grid.map(plt.scatter, alpha=0.5, color='green', marker='^')
    # plt.show()

    # 4.2
    sorted_cores = ['single', 'dual', 'triple', 'quad', 'penta', 'hexa', 'hepta', 'octa']
    diff_cores = pd.Categorical(data['cores'], ordered=True, categories=sorted_cores)
    plt.scatter(data.px_width, data.px_height, s=(diff_cores.codes+1)*10, c=data.price, alpha=0.5, cmap='jet')
    plt.xlabel('px_width')
    plt.ylabel('px_height')
    plt.colorbar(label='price')

    for i,c in enumerate(sorted_cores):
        plt.scatter([], [], c='k', alpha=0.3, s=(i+1)*10, label=c)

    plt.legend(scatterpoints=1, frameon=False, labelspacing=0.5, title='cores')
    plt.title("Relationship between px_width, px_height, price and core")
    plt.show()

    # 4.3
    

if __name__ == "__main__":
    task4()