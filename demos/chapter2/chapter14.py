# This program calculates the area and perimeter of a rectangle

# The object-oriented way
class Rectangle:
    # this function is called a constructor
    # self refers to the current rectangle object
    # width and height are attributes of the rectangle
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # The next two functions are getter methods, they get data
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Create two rectangle objects (instances). This is called instantiation
rect1 = Rectangle(5, 10)
print(f'Rectangle 1 Area: {rect1.area()}')
print(f'Rectangle 1 Perimeter: {rect1.perimeter()}')
rect2 = Rectangle(4, 3)
print(f'Rectangle 2 Area: {rect2.area()}')
print(f'Rectangle 2 Perimeter: {rect2.perimeter()}')

# The non-object-oriented way
width = 5
height = 10
area = width * height
perimeter = 2 * (width + height)
print(f'Rectangle 1 Area: {area}')
print(f'Rectangle 1 Perimeter: {perimeter}')

width = 4
height = 3
area = width * height
perimeter = 2 * (width + height)
print(f'Rectangle 2 Area: {area}')
print(f'Rectangle 2 Perimeter: {perimeter}')