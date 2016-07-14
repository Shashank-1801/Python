"""
Author : shekhars@usc.edu
Date: July 12, 2016
"""

import datetime


coinSol = [9999] * 9999

def coinProb(sumLeft):
    if sumLeft == 0:
        coinSol[0] = 0
        return 0
    elif sumLeft < 1:
        return 9999
    else:
        '''coin_1 = min(coinSol[sumLeft-1], int(coinProb(sumLeft-1)))
        coin_10 = min(coinSol[sumLeft-10], int(coinProb(sumLeft-10)))
        coin_30 = min(coinSol[sumLeft-30], int(coinProb(sumLeft-30)))
        coin_40 = min(coinSol[sumLeft-40], int(coinProb(sumLeft-40)))
        coins = coinSol[sumLeft] = 1 + min(coin_1, coin_10, coin_30, coin_40)
        '''
        coin_1 = min(coinSol[sumLeft-1], int(coinProb(sumLeft - 1)))
        coin_10 = min(coinSol[sumLeft-10], int(coinProb(sumLeft - 10)))
        coin_30 = min(coinSol[sumLeft-30], int(coinProb(sumLeft - 30)))
        coin_40 = min(coinSol[sumLeft-40], int(coinProb(sumLeft - 40)))
        coins = 1 + min(coin_1, coin_10, coin_30, coin_40)
        coinSol[sumLeft] = coins
        #print(coins)
        return coins


def main():
    print("Coin problem for homework assignment")
    a = datetime.datetime.now()
    for c in range(1, 100):
        print(str(c) + " : " + str(coinProb(c)))
        b = datetime.datetime.now()
        print(b-a)
    #print("For 52 cents, Solution is : " + str(coinProb(100)))

    #for x in range(999):
     #   print(coinSol[x])

if __name__ == "__main__":
    main()