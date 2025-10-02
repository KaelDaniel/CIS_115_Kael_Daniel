#this program will calculate the kinetic energy of a moving object

import math

mass = int(input("give the mas of an object: "))
velocity = int(input("give a velocity of an object: "))

def kinetic_energy(mass,velocity):
    return math((mass*0.5)*(velocity**2))

print(kinetic_energy(mass,velocity))