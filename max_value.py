#this program will ask for two inputs, and then print the largest one

num1 = int(input("Enter a number: "))

num2 = int(input("Enter another number: "))

def max(a, b):
    if b > a:
        return b
    else:
        return a

print(f"The largest number inputted is {max(num1, num2)}")