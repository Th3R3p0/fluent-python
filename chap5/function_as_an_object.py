def factorial(n):
    '''returns n!'''
    return 1 if n<2 else n*factorial(n-1)

print(factorial(5))
print(factorial.__doc__)
print(type(factorial))

print()
# use a function through a different name and pass function as argument
fact = factorial
print(fact)
print(fact(5))
print(map(factorial, range(11)))
print(list(map(factorial, range(11))))

