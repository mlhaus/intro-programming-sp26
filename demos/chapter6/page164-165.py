# Variables
breakfast = "Pancakes"
lunch = "Tacos"
dinner = "Lasagna"

# List
meals = ["Pancakes", "Tacos", "Lasagna"]
meals[0] = "Pop tarts" # replaces the first value
meals[1] = "A meat ball sandwich"  # replaces the second value
meals[2] = "A hamburger" # replaces the third value

print(meals) # print the list with quotation marks and brackets
print(*meals, sep=", ") # prints the list without quotation marks and brackets
# prints the values in the list each on a separate line
for meal in meals:
    print(meal + (" are" if(meal[-1] == "s") else " is") + " delicious")

print(meals[0]) # prints the first value
print(meals[1]) # prints the second value
print(meals[2]) # prints the third value
#print(meals[3]) # prints a value that doesn't exist
print(meals[-3]) # prints the third to last value
print(meals[-2]) # prints the second to last value
print(meals[-1]) # prints the last value
print(meals[len(meals) - 1]) # prints the last value
# prints the values in the list each on a separate line
for i in range(len(meals)):
    print(meals[i])

# prints the values in reverse each on a separate line
for i in range(-1, len(meals) * -1 - 1, -1):
    print(meals[i])

data = ["Marc", 45, 71.5]
for val in data:
    print(val)