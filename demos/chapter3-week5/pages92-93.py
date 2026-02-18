print("Type 'exit' to quit.") 
print("=================") 
while (name := input("Your name: ") != "exit"):
    print(f"Hi, {name}!")
print()

print("Enter a negative number to quit.") 
print("=================") 
while (score := float(input("Enter a score: ")) >= 0):
    print(f"You entered a postive number.") 
print("Bye!")