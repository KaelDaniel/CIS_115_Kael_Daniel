#thsi program will check if a word is a palindrome

#the function reverses a word
def isPalidrome(word):
    return word == word[::-1] #return gives the result

#user input
word = input("Enter a string of at least 5 characters: ")
if len(word) < 5: #checks to see if the word is long enough
    print("The string must be at least five characters long.")
else:
    if isPalidrome(word): #if it is a palindrome
        print(f"The string '{word}' is a palindrome.")
    else: #if it's not a palindrome
        print(f"The string '{word}' is NOT a palindrome.")