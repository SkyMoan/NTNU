import random
numbers = []
for i in range(0,35):
    numbers.append(i)

myGuess = []
while len(myGuess) < 7:
    randomNumber = [random.randrange(1, 35)]
    myGuess.append(randomNumber)


def drawNumbers(n):
    winningNumbers = []
    while len(winningNumbers) < 7:
        winningNumber =  [random.randrange(1, 35)]
        winningNumbers.append(winningNumber)
    return winningNumbers
main_result = drawNumbers(7)
extra_result = drawNumbers(3)


def compList(a,b):
    k=0
    for i in range(len(a)):
        if a[i] in b:
            k+=1
    return k   


print("Contratulations, you have: " + str(compList(myGuess,main_result)) + " correct number(s)!!" + " and " +  str(compList(myGuess,extra_result)) + " extranumber(s)")


