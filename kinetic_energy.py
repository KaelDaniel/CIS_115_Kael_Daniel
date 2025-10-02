#this program will calculate the kinetic energy of a moving object

mass = int(input("give the mas of an object: "))
velocity = int(input("give a velocity of an object: "))

def kinetic_energy(mass,velocity):
    ke= (mass*0.5)*(velocity**2)
    return ke

print(kinetic_energy(mass,velocity))