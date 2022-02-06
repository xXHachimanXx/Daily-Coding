"""
This problem was asked by Twitter.

You run an e-commerce website and want to record 
the last N order ids in a log. Implement a data 
structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. 
             i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""

list = []  
    
def record(order_id):
    global list

    list.append(order_id)

def get_last(index):
    return list[len(list) - index]

record(1)
record(2)
record(3)
record(4)
record(5)
record(6)
record(7)
record(8)

assert get_last(3) == 6
assert get_last(5) == 4
assert get_last(len(list)) == 1

"""
Time complexity = O(1)
Space complexity = O(n) -> just one array with n positions
"""