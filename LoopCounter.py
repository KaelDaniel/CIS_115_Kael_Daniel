#this program will have a loop within an function

#user input
times = int(input("how many times do you want it to loop: "))

#this function creates a loop
def print_iterations(val):
    loopcounter = 0
    for _ in range(val):
        loopcounter = loopcounter + 1
    return loopcounter

print(print_iterations(times))