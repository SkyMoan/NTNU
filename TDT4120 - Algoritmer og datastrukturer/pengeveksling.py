from sys import stdin
#stdin = file('input1.txt')

def minCoinsGreedy(coins, value):
    teller = 0
    for coin in coins:
        while (value-coin) >= 0:
            value -= coin
            teller += 1
    return teller

def minCoinsDynamic(coins, value):
    table = [None for x in range(value + 1)]
    table[0] = []
    for i in range(1, value + 1):
        for coin in coins:
            if coin > i: continue
            elif not table[i] or len(table[i - coin]) + 1 < len(table[i]):
                if table[i - coin] != None:
                    table[i] = table[i - coin][:]
                    table[i].append(coin)
    if table[-1] != None:
        return len(table[-1])
    else:
        return None

def canUseGreedy(coins):
        for i in range(len(coins) - 1):
            if coins[i] % coins[i + 1] != 0:
                return False
        return True

Inf = 1000000000
coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()

if method == "graadig" or (method == "velg" and canUseGreedy(coins)):
    for line in stdin:
        print (minCoinsGreedy(coins, int(line)))
else:
    for line in stdin:
        print (minCoinsDynamic(coins, int(line)))
