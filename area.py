import math
def area_of_rectangle(length,breadth):
    return length * breadth
def area_of_sqare(side):
    return side*side
def area_of_circle(radius):
    return math.pi * radius ** 2

length=float(input("Enter the Length of a rectangle:"))
breadth=float(input("Enter the breadth of a rectangel:"))
side=float(input("Enter the side of a square:"))
radius=float(input("Enter the radius of a circle:"))

rectangle_area=area_of_rectangle(length,breadth)
square_area=area_of_sqare(side)
circle_area=area_of_circle(radius)

print("Area of Rectangle is",rectangle_area)
print("Area of sqare:",square_area)
print("Area of cicle",circle_area)
