#this code will ask user to input numbers, until they input a number in the range of 1-100

numberinput = int(input("Please enter a number between 0 and 100: "))

while numberinput >= 0 and numberinput <= 100:
    numberinput = int(input("Please enter a number between 0 and 100: "))
else:
    print("Sorry, the number you entered is out of range!")