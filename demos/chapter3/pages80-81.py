# display a welcome message
print("Welcome to the miles per gallon program\n")

# get input from the user
prompt = "Enter miles driven"
print(prompt, end=": ")
miles_driven = float(input())

prompt = "Enter gallons of gas used"
print(prompt, end=": ")
gallons_used = float(input())

# calculate mpg
if(miles_driven > 0 and gallons_used > 0):
    mpg = round(miles_driven / gallons_used, 2)
    print(f"Miles per gallon is {mpg}")
else:
    print("The miles per gallon and gallons used must be greater than 0")

# display a goodbye message
print("\nGoodbye!")