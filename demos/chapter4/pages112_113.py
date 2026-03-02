from pages110_111 import to_currency

def calc_tax(amount: float, tax_rate = 0.05):
    tax = amount * tax_rate
    return tax

def main():
    sale_price = 100
    tax = calc_tax(sale_price) # Calculate 5% tax
    print(to_currency(tax)) # $5.00

    new_tax = 0.07
    tax = calc_tax(sale_price, new_tax) # Calculate 7% tax
    print(to_currency(tax)) # $7.00


if __name__ == "__main__":
    main()
