"""
Author : shekhars@usc.edu
Date: July 12, 2016
"""

import datetime

infy = 9999
coinSol = [infy] * infy


def coinProb(j):
    if j == 0:
        coinSol[0] = 0
        return 0
    elif j < 1:
        return 9999
    else:
        # calculation for coin 1
        if (j - 1) < 0:
            use_1 = infy
        else:
            use_1 = coinSol[j - 1]
        # calculation for coin 10
        if (j - 10) < 0:
            use_10 = infy
        else:
            use_10 = coinSol[j - 10]
        # calculation for coin 30
        if (j - 30) < 0:
            use_30 = infy
        else:
            use_30 = coinSol[j - 30]
        # calculation for coin 40
        if (j - 40) < 0:
            use_40 = infy
        else:
            use_40 = coinSol[j - 40]
        # calculate the number of coins needed
        coins = 1 + min(use_1, use_10, use_30, use_40)
        return coins


def numberOfCoins(sum):
    for p in range(0, sum+1):
        coinSol[p] = coinProb(p)
    return coinSol[sum]


def main():
    print("Coin problem for homework assignment")
    a = datetime.datetime.now()
    for c in range(1, 61):
        print(str(c) + " : " + str(numberOfCoins(c)))
        b = datetime.datetime.now()
        print(b-a)


if __name__ == "__main__":
    main()