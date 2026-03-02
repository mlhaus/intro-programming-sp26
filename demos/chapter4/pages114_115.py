def calc_tax(amount, tax_rate = 0.07):
    tax = amount * tax_rate
    return tax

def main():
    price = 85
    tax_percent = 0.05
    tax = calc_tax(price, tax_percent)
    amount_owed = price + tax
    print(f"Price: {price}")
    print(f"Tax: {tax}")
    print(f"Amount Owed: {amount_owed}")

if __name__ == "__main__":
    main()