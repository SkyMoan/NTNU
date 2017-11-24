#Komplett liste
def file_to_list(filename):
    dataList=[]
    f = open(filename)
    for line in f:
        lineList = line.split("\t")
        dataList.append(lineList)
    f.close()
    return dataList
result = file_to_list("pricewar.txt")

#Printe ut lista fra oppgave a
for elem in result:
    print (elem)
print( "\n")


#Butikker
def list_stores(dataList):
    storeList = []
    for line in dataList:
        if line[0] not in storeList:
            storeList.append(line[0])
    return storeList
stores = list_stores(result)
print(stores)


#Pris
def sum_prices_stores(dataList,storeList):
    sumStores = [0]*len(storeList)
    for line in dataList:
        storeNr = storeList.index(line[0])
        sumStores[storeNr] += line[2]
    return sumStores
res_sum_prices = sum_prices_stores(result,stores)
print(res_sum_prices)



#Priskrig ladder
def rank_stores(storeList,sumStores):
    switch = True
    while(switch):
        switch = False
        for i in range(len(storeList)-1):
            if sumStores[i+1]<sumStores[i]:
                switch = True
                temp = sumStores[i]
                sumStores[i] = sumStores[i+1]
                sumStores[i+1] = temp
                temp = storeList[i]
                storeList[i] = storeList[i+1]
                storeList[i+1] = temp
    return storeList

def store_analysis(filename):
    dataList = file_to_list(filename)
    storeList = list_stores(dataList)
    sumStores = sum_prices_stores(dataList,storeList)
    print("The total price for shopping per store is:")
    for i in range(len(storeList)):
        print(storeList[i],":",sumStores[i],"kr")

    print("\nThe ranking of stores according to prices is:")
    rankedStores = rank_stores(storeList,sumStores)
    for i in range(len(rankedStores)):
        print(i+1,rankedStores[i])