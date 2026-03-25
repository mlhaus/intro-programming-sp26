student_colors = {} # creates an empty dictionary
student_colors["Max"] = "red"
student_colors["Tyson"] = "blue"
student_colors["Thor"] = "white"
student_colors["Charlotte"] = "black"
student_colors["Angel"] = "black"
student_colors["Colin"] = "pink"
student_colors["Chris"] = "green"

# Chapter 12
for key, value in student_colors.items():
    first_name = key
    fav_color = value
    print(f"{first_name}'s favorite color is {fav_color}")