'''
QUESTION FOR TODAY
Given an array of integers, return a new array such that each element at index i 
of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

def product(numbers:list) -> list:
    # Create a list of 1s that is the same length as given list
    length = len(numbers)
    output = [1 for x in range(length)]

    for i in range(length):
        for j in range(length):
            if i==j:
                continue

            output[i] = output[i] * numbers[j]

    return output

print(product([1, 2, 3, 4, 5]))
print(product([3, 2, 1]))