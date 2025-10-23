#this program will take address information from the user and store it in a dictionary, then print it out in a formatted way

Names_and_Adress = {} #made the dictionary empty to start

#user inputs
city = input("please enter waht city you live in: ") 
state = input("please enter what state you live in: ") 
zip_code = input("please enter the areas zip code: ") 
phone_number = input("please enter your phone number: ") 
first_name = input("please enter your first name: ")
last_name = input("please enter your last name: ")

def print_dictionary(adress): #function to print the dictionary
    print("Address Information:") #header
    adress["First Name"] = first_name #these assign and create the keys and values in the dictionary
    adress["Last Name"] = last_name
    adress["City"] = city
    adress["State"] = state
    adress["Zip Code"] = zip_code
    adress["Phone Number"] = phone_number
    print(adress) #prints the dictionary



print_dictionary(Names_and_Adress) #calls the function to print the dictionary