from sys import stdin
#stdin = file("input.txt")
from heapq import heappush, heappop


def beste_sti(nm, sans):
    start = 0
    sett = set()
    D = {start:sans[0]}
    P = {}
    Q = [(-D.get(0),start)]

    while Q:
        _, u = heappop(Q)
        if(u in sett):
            continue
        sett.add(u)
        for i in range(len(nm[u])):
            if(nm[u][i] == 1):
                d = D.get(u, 0)*sans[i]
                if(d>D.get(i,0)):
                    D[i]=d
                    P[i]=u
                heappush(Q, (-D.get(i, 0), i))
            
    svar = []
    node = n-1
    while node > 0:
        svar.append(str(node))        
        node = P.get(node, -1)
        if node == -1:
            return str(0)
    svar.append(str(node))
    svar.reverse()
    
    
    return "-".join(svar)
        


n = int(stdin.readline())
sansynligheter = [float(x) for x in stdin.readline().split()]
nabomatrise = []
for linje in stdin:
    naborad = [0] * n
    naboer = [int(nabo) for nabo in linje.split()]
    for nabo in naboer:
        naborad[nabo] = 1
    nabomatrise.append(naborad)
print (beste_sti(nabomatrise, sansynligheter))
