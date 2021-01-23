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
    # sorted_cores = ['single', 'dual', 'triple', 'quad', 'penta', 'hexa', 'hepta', 'octa']
    # diff_cores = pd.Categorical(data['cores'], ordered=True, categories=sorted_cores)
    # plt.scatter(data.px_width, data.px_height, s=(diff_cores.codes+1)*10, c=data.price, alpha=0.5, cmap='jet')
    # plt.xlabel('px_width')
    # plt.ylabel('px_height')
    # plt.colorbar(label='price')

    # for i,c in enumerate(sorted_cores):
    #     plt.scatter([], [], c='k', alpha=0.3, s=(i+1)*10, label=c)

    # plt.legend(scatterpoints=1, frameon=False, labelspacing=0.5, title='cores')
    # plt.title("Relationship between px_width, px_height, price and core")
    # plt.show()

    # 4.3
    mobile_data_2 = pd.read_csv('mobile_price_2.csv')
    plt.scatter(mobile_data_2['price_2'], data['price'], marker='^', color='green')
    plt.xlabel('price_2')
    plt.ylabel('price')
    plt.grid()
    plt.title("diffrence between price and price_2")
    # plt.show()

    plt.scatter((mobile_data_2['price_2']/data['price']), data['id'], marker='^', color='green')
    plt.xlabel('price_2/price')
    plt.ylabel('id')
    plt.grid()
    # plt.show()

    data_1 = pd.read_csv('mobile_price_1.csv')
    data_1['price_2/price_1'] = mobile_data_2['price_2']/data_1['price']

    corr = data_1.corr()
    f, ax = plt.subplots(figsize=(8, 6))
    ax.set_title("Heatmap to locate the price_2 based on feature")
    sb.heatmap(corr, cmap="YlGnBu")
    print(corr['camera'])


if __name__ == "__main__":
    task4()
