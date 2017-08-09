import itertools

gen = itertools.takewhile(lambda n: n<3, itertools.count(1, .5))
print(list(gen))

# if you were to not use takewhile, python would try to build a list of endless counter
