"""
Given a list of numbers and a number k, return whether any two 
numbers from the list add up to k.

For example, given [15, 3, 10, 7] and k of 17, return true 
since 10 + 7 is 17

Bonus: Can you do this in one pass?

a + b = k
a = b - k
b = a - k

"""

def add_up_to_k(array, k):
    my_set = set(array)

    for a in array: # for each number 'a' in array - O(n)
        b = (k - a)
        if b in my_set: # I verify if b exists in my set - O(1)
            print("True: {} + {} = {}".format(a, (k-a), k))
            return True

    print("False")

    return False

add_up_to_k([15, 3, 10, 7], 17) # True: 10 + 7 = 17
add_up_to_k([15, 3, 10, 7], 12) # False
add_up_to_k([15, 3, 3, 10, 7], 6) # True: 3 + 3 = 6
add_up_to_k([15, 10, 7, -1], 6) # True: 7 + -1 = 6
add_up_to_k([15, 3, 3, 10, -7, -1, -3], -4) # True: 3 + -7 = -4

"""
Time complexity: O(n)
Space complexity: O(n)
"""