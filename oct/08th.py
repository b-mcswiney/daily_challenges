"""
QUESTION FOR TODAY
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

"""
def add_to_k(numbers:list, k:int) -> bool:
    """
    Searches through list and returns true if 2 numbers add to given k
    """
    for number in numbers:
        to_look_for = k - number
        if to_look_for in numbers:
            return True
        
    return False

print(add_to_k([10, 15, 3, 7], 17))
print(add_to_k([10, 15, 3, 7], 10))
print(add_to_k([10, 15, 3, 7], 11))
print(add_to_k([10, 15, 3, 7, 5], 8))
print(add_to_k([10, 15, 3, 7, 5], 2))


