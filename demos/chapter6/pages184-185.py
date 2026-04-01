import copy

numbers = [8, 1, 9, 2, 6, 7, 9, 8]
print(len(numbers)) # FUNCTION - How many items are in the list? 8
print(numbers.count(9)) # METHOD - How many times does this item show up? 2

# Sort and reverse will permanently change the order of items
# Make a copy before you sort
numbers_copy = copy.deepcopy(numbers)
numbers_copy.sort() # Sort smallest to largest
print(numbers_copy)
numbers_copy.reverse() # Sort largest to smallest
print(numbers_copy)
print(numbers) # Prints the unmodified original

# Sort without making a copy
print(sorted(numbers))
print(numbers)


fruit = ["apple", "banana", "cherry", "BANANA", "orange", "banana"]
print(len(fruit)) # How many items are in the list? 6
print(fruit.count("banana")) # How many times does this item show up? 3

# Sort and reverse will permanently change the order of items
# Make a copy before you sort
fruit_copy = copy.deepcopy(fruit)
fruit_copy.sort(key=str.lower) # Sort alphabetical A-Z ignoring capitalization
print(fruit_copy)
fruit_copy.reverse() # Sort alphabetical Z-A (this cannot ignore capitalization)
print(fruit_copy)
print(fruit) # Prints the unmodified original

# Sort without making a copy
print(sorted(fruit, key=str.lower))
print(fruit)