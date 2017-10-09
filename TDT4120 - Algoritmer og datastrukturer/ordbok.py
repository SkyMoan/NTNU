
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
# -*- coding: utf-8 -*-
from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.children = {}
        self.positions = []

def build(wordlist):
    root = Node()

    # Gå gjennom alle ordene
    for word, position in wordlist:
        current_node = root
        # Gå gjennom ordets noder, og legg dem til hvis de mangler
        for char in word:
            # Hvis noden ikke har denne bokstaven etter seg
            if char not in current_node.children:
                # Lag en ny node med denne bokstaven
                current_node.children[char] = Node()
            # Gå til neste node
            current_node = current_node.children[char]

        # Vi er på den siste bokstaven i ordet, så lagre posisjonen
        current_node.positions.append(position)

    # Returner rot-noden
    return root
    

def positions(word, index, node):
    """Returns all the positions where a word exists"""
    if len(word) == index:
        # Vi har funnet ordet. Returner posisjonen
        return node.positions
    else:
        # Har ikke funnet det enda, returner svaret fra neste node
        if word[index] == '?':
            results = []
            # Gå gjennom children-nodene til denne
            for child in node.children.values():
                try:
                    results += positions(word, index + 1, child)
                except:
                    return []
            return results
        try:
            return positions(word, index + 1, node.children[word[index]])
        except:
            return []

try:
    # Les inn ordene i ordlisten
    words = stdin.readline().split()
    wordlist = []
    pos = 0
    
    # Legg til ord i ordlisten, med tilhørende posisjoner
    for word in words:
        wordlist.append( (word, pos) )
        pos += len(word) + 1

    # Lag DAWG-en
    root = build(wordlist)
    # Gå gjennom søkeordene
    for searchword in stdin:
        searchword = searchword.strip()
        print searchword + ":",
        # Finn alle posisjonene ordet er på
        positions_list = positions(searchword, 0, root)
        # Print dem ut
        positions_list.sort()
        for position in positions_list:
            print position,
        print # newline
except:
    traceback.print_exc()
