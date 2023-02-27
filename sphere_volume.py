#program to output the volume of a sphere using a function
radius=int(input("Enter the radius of the sphere="))
def sphere_volume(radius):
    volume=4/3*3.14*radius*radius*radius
    return volume

print("volume of sphere=",sphere_volume(radius))