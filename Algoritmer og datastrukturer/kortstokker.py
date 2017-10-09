from sys import stdin
from itertools import repeat
#stdin = file("input.txt")

def merge(decks):
    liste = []
    svar = ""
    for i in decks:
        for j in i:
            liste.append(j)
    liste = sorter(liste)
    index, bokstav = zip(*liste)
    for i in range(len(index)):
        svar+=bokstav[i]
    return svar

def sorter(list):
    if list == []: 
        return []
    else:
        pivot = list[0]
        lesser = sorter([x for x in list[1:] if x < pivot])
        greater = sorter([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater


decks = []
for line in stdin:
    (index, list) = line.split(':')
    deck = zip(map(int, list.split(',')), repeat(index))
    decks.append(deck)
print (merge(decks))
