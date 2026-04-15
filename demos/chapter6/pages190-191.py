from functools import reduce

def squareList(nums: list):
    #for num in nums:
    #    num ** 2
    for i in range(len(nums)):
        nums[i] **= 2

numbers = [1, 2, 3, 4, 5]
squareList(numbers)
print(numbers) #[1, 4, 9, 16, 25]


words = ["apple", "banana", "cherry", "date", "elderberry"]

# Map: Apply a function to each element of a list
# Return a new list of modified values.
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

uppercase_words = list(map(str.upper, words))
print(uppercase_words)  # Output: ['APPLE', 'BANANA', 'CHERRY', 'DATE', 'ELDERBERRY']


# Filter: Filter elements of a list based on a condition
# Return a new list with certain values removed
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4], which became [4, 16] when squared

long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)  # Output: ['banana', 'cherry', 'elderberry']

# Reduce: Combine elements of a list into a single value
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

combined_word = reduce(lambda x, y: x + y, words)
print(combined_word)  # Output: applebananacherrydateelderberry