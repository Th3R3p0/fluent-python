l = [10, 20, 30, 40, 50, 60]
print(l[:2])


# slicing: [start:stop:step]
s = 'bicycle'
# slice x steps
print(s[::3])
# slice reverse
print(s[::-1])

print()
invoice = """
123456789012345678901234567890123456789012
1909  Book 1         $9.99    3    $29.97
1910  Book 2         $9.99    1     $9.99
"""
SKU = slice(0, 6)
DESCRIPTION = slice(6, 20)
UNIT_PRICE = slice(20, 30)
QUANTITY = slice(30,34)
ITEM_TOTAL = slice(44, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

# assigning to slices
l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)

# the right side must be iterable even if it is just one item
l[2:4] = [100]

print()
# beware of using a*n when a is a sequence containing mutable items
list1 = [['a']] * 3
print(list1)
# changing item zero in the array modifies all items because they are references to the same item rather than their own
# unique items
list1[0][0]='b'
print(list1)
print()

# correct way to do this
list2 = [['a'] for i in range(3)]
print(list2)
list2[0][0]='b'
print(list2)

