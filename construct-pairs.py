"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) 
returns the first and last element of that pair. For example, 
car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair_received):
    def f(a, b):
        return a

    return pair_received(f)


def cdr(pair_received):
    def f(a, b):
        return b

    return pair_received(f)

print( "({}, {})".format(car(cons(1, 4)), cdr(cons(3, 4))))

"""
Time complexity: O(1)
Space complexity: O(1)
"""