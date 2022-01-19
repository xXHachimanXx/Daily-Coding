"""
Difficult: HARD

This problem was asked by Stripe.

Given an array of integers, find the first missing positive 
integer in linear time and constant space. In other words, 
find the lowest positive integer that does not exist in the 
array. The array can contain duplicates and negative numbers 
as well.

For example, the input [3, 4, -1, 1] should give 2. The input 
[1, 2, 0] should give 3.
"""

def find_missing_first_positive_integer(array):
    biggest = 0

    # Remove negative numbers (and zero) and find,
    # the biggest number of given array - O(n)
    for num in array:
        if num <= 0:
            array.remove(num)
        elif num > biggest:
            biggest = num

    # Create a dictionary with values from 1 to n+2.
    # n+2, because I need consider the number after the biggest number
    # and because my first key is 1 - O(n)
    dict = {}
    for x in range(1, biggest+2):
        dict[x] = 0

    # Increment the respective counters - O(n)
    for x in array:
        dict[x] += 1
    
    # Get the lowest key that have 0 in your counter - O(n)
    lowest_key = -1
    for key, value in dict.items():
        if value == 0 and (lowest_key < 0 or key < lowest_key):
            lowest_key = key

    return lowest_key

lowest = find_missing_first_positive_integer([3, 4, -1, 1])
print(lowest)

lowest = find_missing_first_positive_integer([1, 2, 0])
print(lowest)

"""
Time complexity: O(4*n) = O(n)
Space complexity: O(n + (n+2)) = O(n)
"""