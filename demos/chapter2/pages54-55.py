import locale
locale.setlocale( locale.LC_ALL, '' )
quantity = int(input("Enter the quantity: "))
price = float(input("Enter the price: "))
print(f'{quantity} * {locale.currency(price, grouping=True)} = {locale.currency(quantity * price, grouping=True)}')



miles_driven = 150
gallons_used = 5.875
mpg = round(miles_driven / gallons_used, 2)
print(f"You used {mpg} MPG by driving {miles_driven} miles and using {gallons_used} gallons of gas.")



x = 15
y = input() # input always returns a string
# z = x + y
z = str(x) + y # concatenation
print(z)
z = x + int(y) # addition
print(z)