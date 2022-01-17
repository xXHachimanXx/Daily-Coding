"""
    

For example, if our input was [1, 2, 3, 4, 5], the expected 
output would be [120, 60, 40, 30, 24]. If our input was 
[3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

solution: multiply all numbers of array and divide for the number
at index 'i'

solution 2: multiply all numbers of array if his index is different 
of 'i'

"""

def product(array):
    n = len(array)
    left = [0]*n
    right = [0]*n
    product = []

    # if array has one number, the result will be 0
    if n == 1:
        print(0)
        return

    if n == 2:
        print(array)
        return

    left[0] = 1
    right[n-1] = 1

    # calculate all results at left of the all indexes - O(n)
    for x in range(1, n):
        left[x] = array[x-1] * left[x-1]


    # calculate all results at right of the all indexes - O(n)
    for x in range(n-2, -1, -1):
        right[x] = array[x+1] * right[x+1]
    
    # multiply right values by left values - O(n)
    for x in range(n):
        product.append(left[x] * right[x])

    print(product)

    return product

product([1, 2, 3, 4, 5])
product([1, 2, 3, -4, 5])
product([1, 2, 5])
product([1, 2])
product([2])

"""
eg.: array = [1, 2, 3, 4, 5]

right   =   [  1,  1,  2,  6, 24]      
left    =   [120, 60, 20,  5,  1]
          -------------------------
product =   [120, 60, 40, 30, 24]
"""