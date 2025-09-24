#this code will solve the hypotenuse of a right triangle
import math

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

print(calculate_hypotenuse(a, b))