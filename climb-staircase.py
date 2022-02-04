from tkinter import N


def fib(n):
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)


def climb(n):
    return fib(n+1)


assert climb(4) == 5