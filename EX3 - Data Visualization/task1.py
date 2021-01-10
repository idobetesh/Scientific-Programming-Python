import pandas as pd
import matplotlib.pyplot as plt

# ======================== Task ======================== #

def task1():
    # 1.1
    data = pd.read_csv("./Data/mobile_price_1.csv")

    # 1.2
    print(f"Numinal categorical features => {data.columns[10]} | {data.columns[14]} | {data.columns[18]} | {data.columns[19]}")
    print(f"Ordinal categorical features => {data.columns[11]} | {data.columns[12]} | {data.columns[13]}")

    # 1.3
    data["resolution"] = (data["px_width"] * data["px_height"])

    # 1.4
    inchToCm = 0.3937
    data["DPI_w"] = data["px_width"] / data["sc_w"] * inchToCm

    # 1.5
    data["call_ratio"] = data["battery_power"] / data["talk_time"]

    # 1.6
    data["memory"] = data["memory"] / 1000

    # 1.7
    print(data)
    print(f"describe():\n{data.describe()}")

    plt.plot(data["price"], color = "orange")
    plt.xlabel("time")
    plt.ylabel("Price", color="blue")
    plt.show()


if __name__ == "__main__":
    task1()