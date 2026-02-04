customer_type_output = "Customer type:"
invoice_total_output = "Invoice total:"
discount_output = "Discount:"
amount_due_output = "Amount due:"
first_col_width = 14
second_col_width = 16

customer_type = input("Enter customer type \
            ('R' for Retail or 'W' for Wholesale): ")
invoice_total = float(input("Enter invoice total: "))

if customer_type.lower() == "r":
    if invoice_total >= 250: 
        discount_percent = 0.2
    elif invoice_total >= 100: 
        discount_percent = .1 
    else: 
        discount_percent = 0
elif customer_type.lower() == "w": 
    if invoice_total >= 500: 
        discount_percent = 0.5 
    else: 
        discount_percent = 0.4
else: 
    discount_percent = 0

customer_type_full = "Retail" if customer_type.lower() == "r" \
                        else "Wholesale" if customer_type.lower() == "w" \
                        else "Unknown"
discount = invoice_total * discount_percent
amount_due = invoice_total - discount
print(f"{customer_type_output:<{first_col_width}s} {customer_type_full:<{second_col_width}s}")
print(f"{invoice_total_output:<{first_col_width}s} {invoice_total:>{second_col_width},.2f}")
print(f"{discount_percent:<3.0%} {discount_output:<{first_col_width - 4}s} {discount:>{second_col_width},.2f}")
print(f"{amount_due_output:{first_col_width}s} {amount_due:>{second_col_width},.2f}")