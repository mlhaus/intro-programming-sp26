# Currency formatting source: https://stackoverflow.com/a/320951
import locale
locale.setlocale( locale.LC_ALL, '' )

subtotal = 1200
tax_percent = 0.05 # 5%
tax_amount = subtotal * tax_percent
grand_total = subtotal + tax_amount
# display the results
spec_literal = 15 # This will be used to set the width of the text label.
spec_currency = '>25' # >: Right-align the content. 25: Make the total width of the field 25 characters.

# The first part takes the string "Subtotal:" and formats it to have a width of 15 characters 
# The second part takes a number variable subtotal and formats it as a currency string based on your system's locale settings (e.g., 1200 becomes '$1,200.00').
# The third part takes that currency string and applies the '>25' formatting, right-aligning it within a 25-character space.
print(f"{'Subtotal:':{spec_literal}} \
{locale.currency(subtotal, grouping=True) \
    :{spec_currency}}")

print(f"{'Tax amount:':{spec_literal}} {locale.currency(tax_amount, grouping=True):{spec_currency}}")
print(f"{'Grand total:':{spec_literal}} {locale.currency(grand_total, grouping=True):{spec_currency}}")
# grand_total = subtotal + (subtotal * tax_percent)
# grand_total = subtotal * (1 + tax_percent)
# print("Subtotal:", locale.currency(subtotal, grouping=True ))
# print("Tax amount:", locale.currency(tax_amount, grouping=True ))
# print("Grand total:", locale.currency(grand_total, grouping=True ))



height = 5
width = 3
print(height + width) # 8
print(height - width) # 2
print(height * width) # 15
print(height / width) # 1.66666666666667
print(height ** width) # 5*5*5 = 125 => to the power of
print(height // width) # 1 => quotient
print(height % width) #2 => remainder (aka modulus operator)
