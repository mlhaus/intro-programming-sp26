import random

numbers = [8, 1, 9, 2, 6, 7, 9, 8]
print(min(numbers)) # 1
print(max(numbers)) # 9
print(sum(numbers)) # 50
print(sum(numbers, 100)) # 150, includes the starting accumulator value

fruit = ["apple", "banana", "cherry", "BANANA", "orange", "banana"]
print(min(fruit)) # BANANA (capital letters are "lower" than lowercase letter)
print(max(fruit)) # orange
for i in range (10):
    print(random.choice(fruit)) # print 10 random fruits

random.shuffle(fruit) # permanently randomizes the list
print(fruit)