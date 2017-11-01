import random


def randList(size, lower_bound, upper_bound):
    r_list = []

    while len(r_list) <= size:
        r_list.append(random.randrange(lower_bound,upper_bound))

    return r_list

print(randList(5,0,10))

def compareLists(list1,list2):
    newlist = []
    for number in list1:
        if number in list2:
            newlist.append(number)

    return newlist

print(compareLists([1,2,3,4],[3,4,5,6]))

def multiCompList(lists):
    newList = []
    for number in lists[0]:
        exists = True
        for list in lists[1:]:
            if number not in list:
                exists = False
                break
        if exists:
            newList.append(number)
    return newList
print(multiCompList([[1,2,3,4,5],[3,4,5,6],[5,6,7,8]]))




def evenorOdd(number):
    if number % 2 == 0:
        return 1
    else:
        return 0

lst2 = [2,4,5,6,1,2,3,4,5,6,8,10,5,10,10,10,10,10]

def longestEven(list):
    record = []
    for index in range(len(list)-1):
        if evenorOdd(list[index]) == 1:
            tempRecord = []
            tempRecord.append(list[index])
            while evenorOdd(list[index+1]) == 1:
                index+=1
                tempRecord.append(list[index])
                if(index+1 > len(list)-1):
                    print(list[index])
                    break
            if len(tempRecord) > len(record):
                record = tempRecord
    return record
print(longestEven(lst2))





