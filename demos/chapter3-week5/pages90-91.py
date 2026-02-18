investment = 10000
# i represent the year
for i in range(20):
    # Add 5% interest each year, for 20 years
    yearly_interest = investment * 0.05
    investment += yearly_interest
investment = round(investment, 2)
print(f"Final amount is: {investment}")


i = 0
investment = 10000
while(i < 20):
    # Add 5% interest each year, for 20 years
    yearly_interest = investment * 0.05
    investment += yearly_interest
    i += 1
investment = round(investment, 2)
print(f"Final amount is: {investment}")