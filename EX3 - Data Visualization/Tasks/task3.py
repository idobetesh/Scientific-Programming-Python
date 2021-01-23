import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

# ======================== Task 3 ======================== #

def task3():
    # load data from csv
    data = pd.read_csv("./Data/mobile_price_1.csv")

    # Numinal categorical features => bluetooth | screen | sim
    # Ordinal categorical features => gen | cores | speed | wifi

    # 3.1
    # Ordinal
    # data['gen_ord'] = pd.Categorical(data.cores, ordered=True, categories=[2,3,4]) already a numeric value [2,3,4]
    data['cores_ord'] = pd.Categorical(data.cores, ordered=True, categories=['single', 'dual', 'triple', 'quad', 'penta', 'hexa', 'hepta', 'octa']).codes+1
    data['speed_ord'] = pd.Categorical(data.speed, ordered=True, categories=['low', 'medium', 'high']).codes+1
    data['wifi_ord'] = pd.Categorical(data.wifi, ordered=True, categories=['none', 'a', 'b', 'g', 'n']).codes+1

    # 3.2
    # Numinal
    data['bluetooth_bin'] = pd.Categorical(data.bluetooth, ordered=False, categories=['No', 'Yes']).codes
    data['screen_bin'] = pd.Categorical(data.screen, ordered=False, categories=['LCD', 'Touch']).codes
    data['sim_bin'] = pd.Categorical(data.sim, ordered=False, categories=['Single', 'Dual']).codes

    # 3.3
    corr = data.corr()
    sb.heatmap(corr, vmin=-1, cmap="YlGnBu")
    plt.show()
    print(data.head(30))

    # 3.4
    data.to_csv('mobile_prices_converted.csv', index=False)


if __name__ == "__main__":
    task3()