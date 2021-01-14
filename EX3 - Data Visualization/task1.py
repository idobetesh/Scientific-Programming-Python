import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ======================== Task 1 ======================== #

def task1():
    # 1.1
    data = pd.read_csv("./Data/mobile_price_1.csv")

    # 1.2
    # Numinal categorical features => bluetooth | screen | sim
    # Ordinal categorical features => gen | cores | speed | wifi

    # 1.3
    data["resolution"] = (data["px_width"] * data["px_height"])

    # 1.4
    inchToCm = 0.3937
    data["DPI_w"] = np.where(data["sc_w"] == 0, np.nan, data["px_width"] / data["sc_w"] * inchToCm)

    # 1.5
    data["call_ratio"] = data["battery_power"] / data["talk_time"]

    # 1.6
    data["memory"] = data["memory"] / 1024

    # 1.7
    print(f"describe():\n{data.describe()}")
    
    1.8
    plt.figure("Task 1 - Price Histogram")
    data["price"].hist(color="orange")
    plt.xlabel("Count")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    task1()