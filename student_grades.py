#this program will take student grades and calculate the average of all the grades within the dictionary

x = int(input("Enter grade for Winters: ")) #long line of user inputs for the students grades
y = int(input("Enter grade for Dian: "))
z = int(input("Enter grade for Charles: "))
a = int(input("Enter grade for Bobby: "))
b = int(input("Enter grade for Aly: "))
c = int(input("Enter grade for Nicole: "))

student_grades = {
    "Nicole": c,
    "Aly": b,
    "Bobby": a,
    "Charles": z,
    "Dian": y,
    "Winters": x
} #the dictionary holding the student names and their grades. grades are user inputs
def calculate_average(grades): #function to calculate average grade
    total = sum(grades.values()) #sum all the grades in the dictionary
    count = len(grades) #count the number of students/grades
    average = total / count #calculate average
    return average

print("The average grade is:", calculate_average(student_grades))