fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

# compare this to higher_order_functions.py where you had to define the function reverse
print(sorted(fruits, key=lambda word: word[::-1]))
