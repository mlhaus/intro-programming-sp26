student_colors = [] # creates an empty list
student_colors.append(["Max", "red"])
student_colors.append(["Tyson", "blue"])
student_colors.append(["Thor", "white"])
student_colors.append(["Charlotte", "black"])
student_colors.append(["Angel", "black"])
student_colors.append(["Colin", "pink"])
student_colors.insert(0, ["Chris", "green"])

# Page 171
for i, student in enumerate(student_colors, start = 1):
    first_name = student[0]
    fav_color = student[1]
    print(f"{i}) {first_name}'s favorite color is {fav_color}")