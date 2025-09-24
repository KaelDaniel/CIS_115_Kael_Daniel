#this Program will calculate the angle theta of a right triangle in degrees
import math

#recieve user input for x and y values
x = int(input("Enter side x: "))
y = int(input("Enter side y: "))

#defining the function Atan2 to calculate the angle in degrees
def Atan2(x, y):
    return math.degrees(math.atan(x / y))

#output the result of the function
print(Atan2(x, y))