import csv
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

def plotFeeGains(contract, name):
    fname = "logged_data/" + contract + ".csv"
    with open(fname, "r" , newline='') as f:
        reader = csv.reader(f, delimiter=';')
        header = reader.__next__()
        rows = [row for row in reader]   
    df = DataFrame(data = rows, columns = header)
    t = df['Time'].to_numpy(dtype = np.dtype(float))
    LP = df['LP'].to_numpy(dtype = np.dtype(float))
    k = df['kLast'].to_numpy(dtype = np.dtype(float))

    t_days = (t-t[0])/(60*60*24)
    relative_increase = np.sqrt(k/k[0])*LP[0]/LP - 1

    x = np.expand_dims(t_days[0:len(t_days):len(t_days)-1],axis=1)
    y = relative_increase[0:len(t_days):len(t_days)-1]
    a, _, _, _ = np.linalg.lstsq(x, y, rcond=None)
    a = a[0]

    APR = a*365*100

    plt.plot(t_days, relative_increase*100, 'b.--', markersize=12, linewidth=2)
    plt.plot(t_days, t_days*a*100, 'r:', markersize=12, linewidth=2)
    plt.title(name + " | APR: {:.2f}%".format(APR))
    plt.grid()

def plotPrice(contract, name, stable = 0):
    fname = "logged_data/" + contract + ".csv"
    with open(fname, "r" , newline='') as f:
        reader = csv.reader(f, delimiter=';')
        header = reader.__next__()
        rows = [row for row in reader]   
    df = DataFrame(data = rows, columns = header)
    t = df['Time'].to_numpy(dtype = np.dtype(float))
    r1 = df['Reserve 1'].to_numpy(dtype = np.longdouble)
    r2 = df['Reserve 2'].to_numpy(dtype = np.longdouble)

    t_days = (t-t[0])/(60*60*24)
    if stable == 0:
        price = r2/r1
    else:
        price = r1/r2

    plt.plot(t_days, price, 'b.--', markersize=12, linewidth=2)
    plt.title(name)
    plt.grid()

def printReservesPerLP(contract, name):
    fname = "logged_data/" + contract + ".csv"
    with open(fname, "r" , newline='') as f:
        reader = csv.reader(f, delimiter=';')
        header = reader.__next__()
        rows = [row for row in reader]   
    df = DataFrame(data = rows, columns = header)
    LP = df['LP'].to_numpy(dtype = np.longdouble)
    r1 = df['Reserve 1'].to_numpy(dtype = np.longdouble)
    r2 = df['Reserve 2'].to_numpy(dtype = np.longdouble)

if __name__ == "__main__":
    names = ["UST-BUSD", "USDT-BUSD", "BUSD-BNB", "BTCB-BUSD", "MNFLX-UST", "MCOIN-UST"]
    contracts = ["0x05faf555522Fa3F93959F86B41A3808666093210", "0x7EFaEf62fDdCCa950418312c6C91Aef321375A00", 
        "0x58F876857a02D6762E0101bb5C46A8c1ED44Dc16", "0xF45cd219aEF8618A92BAa7aD848364a158a24F33", 
        "0x91417426C3FEaA3Ca795921eB9FdD9715ad92537", "0xBCf01a42f6BC42F3Cfe81B05519565044d65D22a"]


    plt.figure(figsize=(10,5))
    n = 2
    m = 3
    for i, contract in enumerate(contracts):
        plt.subplot(n,m,i+1)
        plotFeeGains(contract, names[i])
        if i % m == 0:
            plt.ylabel("Relative increase (%)")
        if i >= (n-1)*m:
            plt.xlabel("Time (days)")
    
    plt.tight_layout()

    # names = ["MAMZN-UST", "MGOOGL-UST", "MNFLX-UST", "MTSLA-UST", "MCOIN-UST"]
    # contracts = ["0xC05654C66756eBB82c518598c5f1ea1a0199a563", "0xA3BfBbAd526C6B856B1Fdf73F99BCD894761fbf3",
    #     "0x91417426C3FEaA3Ca795921eB9FdD9715ad92537", "0xEc6b56a736859AE8ea4bEdA16279Ecd8c60dA7EA", 
    #     "0xBCf01a42f6BC42F3Cfe81B05519565044d65D22a"]
    # stable = [1,1,1,1,1]
    # plt.figure(figsize=(10,5))
    # n = 2
    # m = 3
    # for i, contract in enumerate(contracts):
    #     plt.subplot(n,m,i+1)
    #     plotPrice(contract, names[i], stable[i])
    #     if i % m == 0:
    #         plt.ylabel("Price (UST)")
    #     if i >= (n-1)*m:
    #         plt.xlabel("Time (days)")
    
    # plt.tight_layout()

    # printReservesPerLP("0xBCf01a42f6BC42F3Cfe81B05519565044d65D22a", "MCOIN-UST")
    plt.savefig("figure.jpg", dpi=600)
    # plt.show()

    