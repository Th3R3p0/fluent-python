symbols = "$%^&@"

# listcomp example
listcomp = [ord(symbol) for symbol in symbols]
print(listcomp)

# genexp example
genexp = tuple(ord(symbol) for symbol in symbols)
print(genexp)

# "genexps yields items one by one using the iterator protocol instead of building a whole list just to
# feed another constructor"

# use a generator expression if all you're doing is iterating once. If you want to store and use the generated results,
# then you're probably better off with a list comprehension.
# http://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehension

# this is using a generator expression
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
