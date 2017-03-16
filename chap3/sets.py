# a set is a collection of unique objects
haystack = set('a b c d e f g h i j k'.split())
needles = set('a d z'.split())

# sets allows returning unions, intersections and differences
found = len(needles & haystack)
print(found)

# if you didn't use sets it would look something like this:
found=0
for n in needles:
    if n in haystack:
        found += 1
print(found)

# however, there is a cost in generating the needle and haystack sets
# you can also define a set
s = {'a', 'b', 'c'}
