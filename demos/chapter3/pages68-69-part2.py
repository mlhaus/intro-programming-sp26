day_of_week = "Saturday"
is_weekend = day_of_week == "Saturday" or day_of_week == "Sunday"
print("Is it the weekend?", is_weekend)
print("Is it a weekday?", not is_weekend)

outside_temperature = 76
is_raining = True
wear_jacket = outside_temperature < 64 or is_raining
print("Should I wear a jacket?", wear_jacket)

hour_of_day = 10 # 10am
             # This first checks if the current time is between 10pm and midnight
             # Then it checks if the current time is between midnight and 6am
go_to_sleep = hour_of_day >= 22 and hour_of_day < 24 \
                or hour_of_day >= 0 and hour_of_day <= 6
print("Should you be asleep?", go_to_sleep)

own_a_cat = False
own_a_dog = True
feed_your_pet = (own_a_cat or own_a_dog) and hour_of_day == 5
print("Do you need to feed your pet?", feed_your_pet)