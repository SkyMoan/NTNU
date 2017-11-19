def myst2(m):
    for y in range(len(m)):
        for x in range(len(m[0])):
            if y==0 or y==len(m)-1:
                m[y][x] = 0
            elif x==0 or x==len(m)-1:
                m[y][x] = 0
    return m

m= [[1,2,3,4,5],
    [2,3,4,5,6],
    [3,4,5,6,7],
    [4,5,6,7,8],
    [5,6,7,8,9]]

m = myst2(m)

#print(m)

def myst3(s):
    a = ''
    for x in range(len(s)-1,-1,-2):
        a+= s[x]
    return a

print(myst3("xsidrwteasMc hedhfT"))

def myst4(x,y,z):
    if y<z:
        return
        myst4(x*x,y+1,z)
    else:
        return x

print(myst4(2,1,4))