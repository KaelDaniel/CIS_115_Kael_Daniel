#this program will validate a credit card number using the algorithm mod 10

#user input for credit card number
CC = int(input("Enter your credit card number: "))

#defining the function to validate credit card number
def ValidateCreditCard(ccNum):
    ccNumlist = str(ccNum) #converting credit card number to string for easier manipulation
    reverse = ccNumlist[::-1] #reversing the string to make it easier to apply the mod 10 algorithm
    sum1 = 0 #this is for the numbers that are doubled
    sum2 = 0 #this is for the numbers that are not doubled

    for num in range(len(reverse)): #iterating through each digit in the reversed credit card number
        digit = int(reverse[num]) #converting each character back to integer for calculation
        if num % 2 == 1: #checking if the position is odd (considering 0-based index)
            digit *= 2 #doubling the digit
            if digit > 9: #if the doubled digit is greater than 9, subtract 9 from it
                digit -= 9
            sum1 += digit
        else:
            sum2 += digit
    
    total = sum1 + sum2
    
    if total % 10 == 0: #checking if the total modulo 10 is 0
        print("the credit card number " + str(ccNum) + " is valid.")
    else:
        print("Invalid credit card number.")

#checking the length of credit card number, and if length is valid then beginning validation of card number
if len(str(CC)) < 13 or len(str(CC)) > 16:
    print("Invalid credit card number length.")
else: 
    ValidateCreditCard(CC)