#!/usr/bin/env python3
# display a welcome message 
print("The Invoice program") 
print()

# get user entries
customer_type = input("Enter customer type (retail [r]/wholesale [w]):\t")
invoice_total = -1
while invoice_total <= 0:
    invoice_total = float(input("Enter invoice total:\t\t"))
print()

# determine discounts for Retail customers
if customer_type.lower() == "r":
    if invoice_total > 0 and invoice_total < 100: 
        discount_percent = 0
    elif invoice_total >= 100 and invoice_total < 250: 
        discount_percent = .1
    elif invoice_total >= 250 and invoice_total < 500: 
        discount_percent = .2
    elif invoice_total >= 500: 
        discount_percent = .25
# determine discounts for Wholesale customers
elif customer_type.lower() == "w":
    if invoice_total > 0 and invoice_total < 500:
        discount_percent = .4 
    elif invoice_total >= 500: 
        discount_percent = .5
# set discount to zero if neither Retail or Wholesale
else:
    discount_percent = 0

# calculate discount amount and new invoice total
discount_amount = round(invoice_total * discount_percent, 2)
new_invoice_total = invoice_total - discount_amount

# display the results
right_column_width = 10
num_of_decimals = 2
print(f"Invoice total:\t\t{invoice_total:>{right_column_width},.{num_of_decimals}f}")
print(f"Discount percent:\t{discount_percent:>{right_column_width},.{num_of_decimals}f}")
print(f"Discount amount:\t{discount_amount:>{right_column_width},.{num_of_decimals}f}")
print(f"New invoice total:\t{new_invoice_total:>{right_column_width},.{num_of_decimals}f}")
print()
print("Bye!")