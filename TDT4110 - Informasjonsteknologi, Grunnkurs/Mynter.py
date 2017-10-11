
coin_types = [1, 5, 10, 20]

def count_coins(coins):
    total= 0
    for coin in coins:
        total+=coin
    return total


liste = [12, 23, 34, 45]

def numCoins(lst):
    newlst = []

    for l in lst:
        summ = l

        countobj = {}
        for t in coin_types:
            countobj[str(t)] = 0

        while summ > 0:
            for t in coin_types:
                if summ >= t:
                    summ -= t
                    countobj[str(t)] += 1
        newlst.append(countobj)
    return newlst

print(numCoins(liste))

