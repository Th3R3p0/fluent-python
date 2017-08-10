import itertools

print('chain')
# chain(it1, ... itN)
print(list(itertools.chain('ABC', range(2))))
print(list(itertools.chain(enumerate('ABC'))))

print('chain.from_iterable')
# chain.from_iterable(it)
print(list(itertools.chain.from_iterable((enumerate('ABC')))))

print('zip')
# zip(it1, ..., itN)
print(list(zip('ABC', range(5))))
print(list(zip('ABC', range(5), [10, 20, 30, 40])))

print('zip_longest')
# zip_longest(it1, ..., itN, fillvalue=None)
print(list(itertools.zip_longest('ABC', range(5))))
print(list(itertools.zip_longest('ABC', range(5), fillvalue='?')))

print('product')
# product(it1, ..., itN, repeat=1)
print(list(itertools.product('ABC', range(2))))

suits = 'spades hearts diamonds clubs'.split()
print(list(itertools.product('AK',suits)))
print(list(itertools.product('ABC')))
print(list(itertools.product('ABC', repeat=2)))
print(list(itertools.product(range(2), repeat=3)))

rows = itertools.product('AB', range(2), repeat=2)
for row in rows: print(row)
