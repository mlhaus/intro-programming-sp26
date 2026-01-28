firstName = "😹Marc"
lastName = "Hauschildt"
age = 45
fullName = "My name is " + firstName + " " + lastName + ". " # Concatenates firstName and lastName with a space in between
fullName += "I am " + str(age) + " years old."  # Appends age to fullName
print(fullName)
fullName = f"My name is {firstName} {lastName}. I am {age} years old."  # Uses an f-string to format fullName
print(fullName, end=" ... ")
print("Good bye")