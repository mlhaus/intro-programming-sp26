#!/usr/bin/env python3

import locale
locale.setlocale(locale.LC_ALL, "en_US")
        
def calculate_future_value(monthly_investment, yearly_interest_rate, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def display_welcome_message():
    print("Welcome to the Future Value Calculator")
    print()

def get_user_input():
    # get input from the user
    monthly_investment = float(input("Enter monthly investment:\t"))
    yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
    years = int(input("Enter number of years:\t\t"))
    return monthly_investment, yearly_interest_rate, years

def to_currency(val):
    return locale.currency(val, grouping=True)

def main():
    display_welcome_message()
    choice = "y"
    while choice.lower() == "y":
        monthly_investment, yearly_interest_rate, years = get_user_input()

        # get and display future value
        future_value = calculate_future_value(monthly_investment, yearly_interest_rate, years)

        print(f"Future value:\t\t\t{to_currency(future_value)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()