# a higher order function takes a function as an argument or returns a function
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))

def reverse(word):
    return word[::-1]

print(sorted(fruits, key=reverse))
