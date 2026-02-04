fuel_in_tank = 15
mpg = 21
distance_to_travel = 300
# enough_fuel_in_tank = fuel_in_tank * mpg >= distance_to_travel
enough_fuel_in_tank = fuel_in_tank >= distance_to_travel / mpg
print("Do I have enough fuel?", enough_fuel_in_tank)

age = 12
registered_to_vote = True
can_vote = age >= 18 and registered_to_vote
print("Can I vote?", can_vote)

numerator = 2
denominator = 0
is_positive = denominator != 0 and numerator / denominator > 0
print("Is the number positive?", is_positive)


month = "October"
day_of_month = 31
is_halloween = month == "October" and day_of_month == 31
print("Is it Halloween?", is_halloween)

has_costume = True
can_trick_or_treat = is_halloween and age < 14 and has_costume
print("Can I trick-or-treat?", can_trick_or_treat)

month = "February"
day_of_month = 4
is_valentines_day = month == "February" and day_of_month == 14
print("Is it valentine's day?", is_valentines_day)