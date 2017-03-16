import bisect

a = [2, 5, 3, 8, 4]
print(a)
a.sort()
print(a)

# sorting can be an expensive. rather than appending a new item to the end of the list and then sorting again,
# you can use bisect.insort to keep the list sorted
bisect.insort(a, 4)
print(a)
