# if only storing numbers, use an array. array.array is more efficient than a list

from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
fp = open('floats.bin', 'wb')
# saving using tofile is 7 times faster than writing one float per line in a text file
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
# using fromfile is 60 times faster than reading numbers from a text file
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
assert floats == floats2
# this example also saves over 50% disk space for the file
