#this program will calculate the number of joules in any given mass

#user input for mass
mass = float(input("Enter the mass of the object in kilograms: "))

#function to calculate energy in joules
def calculate_energy(mass):
    c = 3 * (10**8)
    joules = mass * (c**2)
    return joules

#print the result
print("The number of joules in", mass, "kilograms is", calculate_energy(mass))