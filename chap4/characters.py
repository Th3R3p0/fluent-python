# when as a string, "café" has 4 unicode characters
# However, when encoded with utf-8, it has 5 bytes because the é is stored in 2 bytes as opposed to one

b = 'café'
print(len(b))
b = b.encode('utf-8')
print(len(b))
