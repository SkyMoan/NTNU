def number_of_lines(filename):
    n = 0
    f = open(filename, "r")
    for line in f:
        n+=1
    f.close()
    return n


#Veldig eksamensrelevant! Må jobbes mer med!!!!

def number_frequency(filename):
    num_freq = {}
    f = open(filename,"r")
    num = f.readlines()
    for n in num:
        num_freq[n[0]] =num_freq.get(n[0],0)+1
    f.close()
    return num_freq

num_set = number_frequency("numbers.txt")
for e in sorted((num_set)):
    print(e+": " + str(num_set[e]))

