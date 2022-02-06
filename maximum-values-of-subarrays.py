"""
This problem was asked by Google.

Given an array of integers and a number k, 
where 1 <= k <= length of the array, compute 
the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] 
and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can 
modify the input array in-place and you do not 
need to store the results. You can simply print 
them out as you compute them.
"""

def maximum(array, k):
    temp_array = [array.pop(0), array.pop(0), array.pop(0)] # k positions
    
    for num in array: # O(n)
        print(max(temp_array))
        temp_array.pop(0)
        temp_array.append(num)
        
    print(max(temp_array))
    

maximum([10, 5, 2, 7, 8, 7], 3)
print(10*'-')
maximum([10, 5, 2, 7, 8, 7, 9, 2, 11, 2, 1, 0], 4)

"""
Time complexity = O(n)
Space complexity = O(k)
"""