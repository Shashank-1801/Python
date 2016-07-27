"""
Author : shekhars@usc.edu
Date: July 12, 2016
"""

import datetime


infy = 99999
p = [infy]*infy
lastCoinUsed = [infy]*infy

p[0] = 0


def coinProb(c):
    for j in range(1, c+1):
        if c == 0:
            return 0
        elif c < 1:
            return infy
        else:
            # calculation for coin 1
            if (j-1) < 0:
                use_1 = infy
            else:
                use_1 = p[j-1]
            # calculation for coin 10
            if (j - 10) < 0:
                use_10 = infy
            else:
                use_10 = p[j - 10]
            # calculation for coin 30
            if (j - 30) < 0:
                use_30 = infy
            else:
                use_30 = p[j - 30]
            # calculation for coin 40
            if (j - 40) < 0:
                use_40 = infy
            else:
                use_40 = p[j - 40]
            # find min of the coins
            minVal = min(use_1, use_10, use_30, use_40)
            if minVal == use_1:
                lastCoinUsed[j] = 1
            elif minVal == use_10:
                lastCoinUsed[j] = 10
            elif minVal == use_30:
                lastCoinUsed[j] = 30
            else:
                lastCoinUsed[j] = 40
            # total coins used will be 1 + coin used earlier
            coins = 1 + minVal
            p[j] = coins
            #print(j)
    return coins


def main():
    print("Coin problem for homework assignment-iterative Solution")
    a = datetime.datetime.now()
    # print("Coins needed are : " + str(coinProb(21)))
    for c in range(1, 61):
        print("For " + str(c) + ", Coins needed are : " + str(coinProb(c)))
        rem = c
        while rem != 0:
            print(lastCoinUsed[rem], end=",")
            v = lastCoinUsed[rem]
            rem = rem - v
        print()
        b = datetime.datetime.now()
        print(b-a)


if __name__ == "__main__":
    main()
