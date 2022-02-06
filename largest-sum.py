"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns 
the largest sum of non-adjacent numbers. Numbers can be 
0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we 
pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since 
we pick 5 and 5.
"""

def largest_sum_of_non_adjacent_numbers(array=[]):
    incl = 0
    excl = 0
    excl_new = None

    for num in array: # O(n)
        if incl > excl:
            excl_new = incl
        else:
            excl_new = excl
        
        incl = excl + num
        excl = excl_new
    
    return incl if incl > excl else excl

print( largest_sum_of_non_adjacent_numbers([2, 4, 6, 2, 5]) )
print( largest_sum_of_non_adjacent_numbers([5, 1, 1, 5]) )

"""
Time complexity = O(n)
Space complexity = O(n) -> just one array with n positions
"""