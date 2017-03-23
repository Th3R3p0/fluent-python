# this example uses a struct and memory to inspect a GIF image header

import struct


fmt = '<3s3sHH'
with open('happy.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(bytes(header))
print(struct.unpack(fmt, header))
del header
del img
