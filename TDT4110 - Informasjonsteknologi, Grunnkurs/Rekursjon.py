import math

def recursive_sum(n):
    sum = 0
    for i in range(0,n+1):
        sum+=i
    return sum
print(recursive_sum(5))

numberlist = [3,4,5,6,3,4,5,1,2,3,4,5,6,7,]
def find_smallest_element(numbers):
    smallest = math.inf
    for i in(numbers):
        if i < smallest:
            smallest = i
    return smallest
print((find_smallest_element(numberlist)))

sorted_numbers = [1,2,3,4,5,6,7,8,9,10]
number = 5

def binary_search(numbers, element):
    for i in numbers:
        if i == element:
            return numbers.index(i)
print(binary_search(sorted_numbers,number))
