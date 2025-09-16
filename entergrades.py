#this program will prompt the user to enter how many grades they want to enter, and then prompt them to enter what the grades are
# it will then print out how many grades they entered

howmanygrades = input("Would you like to enter your Grade(s)? (type y for yes): ")

while howmanygrades == 'y':
    grade = input("what is the grade: ")

    howmanygrades = input("would you like to input another grade? (type y for yes): ")