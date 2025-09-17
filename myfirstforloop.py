#this program will ask the user to input how many times they want the for loop to run
# it will then print out how many times the loop ran

forloopcount = int(input("how many times do you want the for loop to run: "))

for count in range(forloopcount):
    print(f"for loop has run {count + 1} times")