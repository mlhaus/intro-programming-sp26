meals = []
meals.append("Waffles") # add to the end of the list
meals.append("Chicken Salad") # add to the end of the list
meals.append("Chicken Salad") # add to the end of the list
meals.append("Chili") # add to the end of the list
meals.insert(2, "Ice Cream") # adds a value between the second and third values
meals.remove("Chicken Salad") # Removes the first instance of that value
meals.pop() # Removes the last item from the list
meal = meals.pop(0) # Removes the item at a specific index
print(*meals, sep=", ")
print(meal)
i = meals.index("Ice Cream")
print(i) # Even though we inserted ice cream at index 2, we removed the first Chicken Salad and Waffles
meals.append(meal) # Puts waffles back at the end
i = meals.index("Waffles")
print(i) # This would cause a ValueError if the value didn't exist in the list