# filtering generator functions

a = 'Aardvark'

# returns True or False if a characters is a vowel
def vowel(c):
  return c.lower() in 'aeiou'

print('filter')
# filter(predicate, it)
# will only display characters that return True from the vowel function 
print(list(filter(vowel, a)))

import itertools
print('filterfalse')
# filterfalse(predicate, it)
# will only yield characters that return False from the vowel function
print(list(itertools.filterfalse(vowel, a)))

print('dropwhile')
# dropwhile(predicate, it)
# will yield all items after one false value is matched
print(list(itertools.dropwhile(vowel, a)))

print('takewhile')
# takewhile(predicate, it)
# will yield only items that are True and drop the rest after a False is matched
print(list(itertools.takewhile(vowel, a)))

print('compress')
# compress(it, selector_it)
# consumes two iterables in parallel; will yield items from it when selector_it is True
print(list(itertools.compress(a, (1,0,1,1,0,1))))

print('islice')
# islice takes (iterator, stop) or (iterator, stop, stop, step=1)
# the following will top after 4 characters
print(list(itertools.islice(a, 4)))
# the following will start at 4 index and stop at 7 index
print(list(itertools.islice(a, 4, 7)))
# the following will start at 1 index and stop at 7 index stepping by 2
print(list(itertools.islice(a, 1, 7, 2)))

