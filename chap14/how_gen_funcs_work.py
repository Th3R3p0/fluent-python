# any function that contains the yield keyword is a generator function
# usually the body of a generator function has a loop, but not necessarily

# generator fuctions `yield` or `produce` values
# other functions `return` values

def gen_123():
  yield 1
  yield 2
  yield 3
  yield 4

print(gen_123)
print(gen_123())

for i in gen_123():
  print(i)

g = gen_123()
print(g)
print(next(g))
print(next(g))
print(next(g))

def gen_AB():
  print('start')
  yield 'A'
  print('continue')
  yield 'B'
  print('end.')

for c in gen_AB():
  print('-->', c)

