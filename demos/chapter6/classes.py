# Chapter 14
class Person:
    # constructor
    def __init__(self, first_name, fav_color):
        self.first_name = first_name
        self.fav_color = fav_color
    # getters (accessors)
    def get_first_name(self):
        return self.first_name
    
    def get_fav_color(self):
        return self.fav_color


student_colors = [] # creates an empty list
student_colors.append(Person("Max", "red"))
student_colors.append(Person("Tyson","blue"))
student_colors.append(Person("Thor", "white"))
student_colors.append(Person("Charlotte", "black"))
student_colors.append(Person("Angel", "black"))
student_colors.append(Person("Colin", "pink"))
student_colors.append(Person("Chris", "green"))


for student in student_colors:
    print(f"{student.get_first_name()}'s favorite color is {student.get_fav_color()}")