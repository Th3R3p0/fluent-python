for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

print('\n')
# error handling
city = 'São Paulo'
print(city.encode('utf-8'))
print(city.encode('utf-16'))
print(city.encode('iso8859_1'))
print()

# the following would error out:
# print(city.encode('cp437'))

# Traceback (most recent call last):
#   File "/Users/justinmassey/Documents/code/fluent-python/chap4/codecs.py", line 12, in <module>
#     print(city.encode('cp437'))
#   File "/Users/justinmassey/virtualenvs/fluent-python/bin/../lib/python3.6/encodings/cp437.py", line 12, in encode
#     return codecs.charmap_encode(input,errors,encoding_map)
# UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>

# the following handles the error
print(city.encode('cp437', errors='ignore'))
print(city.encode('cp437', errors='replace'))
print(city.encode('cp437', errors='xmlcharrefreplace'))
print()

# the following deals with UnicodeDecodeError
octets = b'Montr\xe9al'
print(octets.decode('cp1252'))
print(octets.decode('iso8859_7'))
print(octets.decode('koi8_r'))

# the following would error out
# print(octets.decode('utf_8'))
#
# Traceback (most recent call last):
#   File "/Users/justinmassey/Documents/code/fluent-python/chap4/codecs.py", line 35, in <module>
#     print(octets.decode('utf_8'))
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5: invalid continuation byte

print(octets.decode('utf-8', errors='replace'))
print()

# BOM: Byte Order Mark
# BOMs are needed to specify if the CPU is using little endian where the LSB comes first ex: [0,1] vs [1,0]
u16 = 'El Niño'.encode('utf_16')
print(u16)
# the "xffxfe" denotes the BOM stating that it is using little ending byte ordering
# the following is an example of the bytes in LE vs BE (see the abbreviations after utf_16
u16le = 'El Niño'.encode('utf_16le')
print(list(u16le))
u16be = 'El Niño'.encode('utf_16be')
print(list(u16be))
