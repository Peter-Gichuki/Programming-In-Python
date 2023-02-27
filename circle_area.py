#program to output area of a circle using a function

radius=int(input("Enter the radius of the circle="))

def circle_area(radius):
    area=3.142*radius*radius
    return area

print("Area of the circle=",circle_area(radius))
