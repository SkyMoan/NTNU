liste1 = [1,2,3,4,5,1,2,3,4,1,5,6,1,2,7,7,5,8,1,9,3,3,3,10,4,1]

liste2 = [1,2,4,6,7,5,]

def allUnique(lst):
    if len(lst) == len(set(lst)):
        return True
    else:
        return False

print(allUnique(liste1))

def removeDuplicates(lst):
    return list(set(lst))
print(removeDuplicates(liste1))

def inAbutnotB(a,b):
    return set(a) - set(b)
print(inAbutnotB(liste1,liste2))