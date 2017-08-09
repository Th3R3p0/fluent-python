import itertools

gen = itertools.count(1, .5)
print(next(gen))
print(next(gen))
print(next(gen))

# the itertools, count never stops
