from collections import namedtuple

a = (2, 4)
print(a)


# tuple unpacking
b, c = a
print(b)
print(c)

# assign rest of values in tuple to a tuple
d, e, *rest = range(5)
print(d, e, rest)

# unpacking nested tuples
metro_areas = [
    ('Tokyo', 'JP', 36.393, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (40.808611, -74.020386))
]

print()
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (lattitude, longitude) in metro_areas:
    if longitude >= 0:
        print(fmt.format(name, lattitude, longitude))

print()

# named tuples
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print()
print(City._fields)

print()
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())

print()
for key, value in delhi._asdict().items():
    print(key + ':', value)
