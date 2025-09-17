#this program will prompt the user to enter how many grades they want to enter, and then prompt them to enter what the grades are
# it will then print out how many grades they entered

count = 0

howmanygrades = int(input("how many grades will you enter: "))

while howmanygrades > count:
    count = count + 1

    grade = int(input("what is the grade: "))


    if count >= howmanygrades:
        print(f"You have entered {howmanygrades} grades")