liste1 = [1,2,3,4,5]
tall = 4


def separate(numbers,threshold):
    less= []
    greater = []
    for i in numbers:
        if i < threshold:
            less.append(i)

        elif i >= threshold:
            greater.append(i)

    return less, greater
print(separate(liste1, tall))


def multiplication_table(n):
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            print(row * col, "\t", end="")
        print()
multiplication_table(tall)
