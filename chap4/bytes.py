cafe = bytes('café', encoding='utf_8')
print(cafe)
print(cafe[0])
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])

print(bytes.fromhex('31 4B CE A9'))
# for bytes in the printable ascii range (from space to ~) the ASCCI characters themeselves are used
# for bytes corresponding to tab, newline, cariage return and \, the escape sequences are used (\t, \n, \r and \\)
# for every other byte, the hexadecimal escape sequence is used. for ex a null byte: \x00
