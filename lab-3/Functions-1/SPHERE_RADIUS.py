import math

def sphere_radius(radius:float):
    return (4/3)*math.pi*pow(radius,3)

print(round(sphere_radius(3),3))