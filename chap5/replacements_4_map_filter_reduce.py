from functools import reduce
from operator import add

def factorial(n):
    '''returns n!'''
    return 1 if n<2 else n*factorial(n-1)

fact = factorial

# map and filter functions vs list comprehensions and generator expressions
print(list(map(fact, range(6))))
print([fact(n) for n in range(6)])
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2])

# reduce function vs sum function - readability and performance are better when using sum function
print()
print(reduce(add, range(100)))
print(sum(range(100)))
