# mapping generator functions

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

import itertools

print('accumulate')
# accumulate(it, [func])
# yields accumulated sums
print(list(itertools.accumulate(sample)))
# yields the minimum item
print('accumulate - min')
print(list(itertools.accumulate(sample, min)))
# yields the maximum item
print('accumulate - max')
print(list(itertools.accumulate(sample, max)))

import operator
print('accumulate - mul')
# yields the multiplied values
print(list(itertools.accumulate(sample, operator.mul)))
print('accumulate - mul - range')
print(list(itertools.accumulate(range(1,11), operator.mul)))

print('enumerate')
# enumerate(iterable, start=0)
print(list(enumerate('albatroz', 1)))

print('map')
# map(func, it1, [it2, ..., itN])
print(list(map(operator.mul, range(11), range(11))))
print(list(map(operator.mul, range(11), [2, 4, 8])))

print('starmap')
# starmap(func, it)
print(list(itertools.starmap(operator.mul, enumerate('abatroz', 1))))
print(list(itertools.starmap(lambda a, b: b/a, enumerate(itertools.accumulate(sample), 1))))

