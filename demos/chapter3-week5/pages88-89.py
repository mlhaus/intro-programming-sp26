
sum = 0
count = 0
min = 1
max = 10
print(f"Enter numbers between {min} and {max} on separate lines. \
    Enter a non-number to stop.") # The non-number is the sentinel
while True:
    try:
        val = float(input())
    except ValueError:
        break # stop the loop
    if(val < min or val > max):
        continue # restart the loop if the number entered is out of range
    sum += val
    count += 1
print(f"You entered {count} numbers between {min} and {max}")
if(count > 0):
    print(f"Sum = {round(sum, 3)}")
    print(f"Average = {round(sum / count, 3)}")
print("Goodbye")
print()

# Calculate miles per gallon
more = "y" # flag variable
while more.lower() == "y":
    miles_driven = float(input("Enter miles driven:\t\t")) 
    gallons_used = float(input("Enter gallons of gas used:\t"))

    # validate input 
    if miles_driven <= 0 or gallons_used <= 0:
        print("Both entries must be greater than zero. Try again.\n") 
        continue # restart the loop
    
    mpg = round(miles_driven / gallons_used, 2) 
    print("Miles Per Gallon:", mpg, "\n")

    more = input("Continue? (y/n): ") 
    print()
print("Okay, bye!")
print()


# Square a number
print("\nEnter 'exit' when you're done.") # exit is the sentinel
data = input("Enter an integer to square: ") 
while data.lower() != "exit":
    i = int(data)
    print(i, "squared is", i * i, "\n") 
    data = input("Enter an integer to square: ") 
print("Okay, bye!")
print()