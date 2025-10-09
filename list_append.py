#this program will append a value to a list and prompt the user if with a y or n
#and once they input n the whole list will be printed out

#user inputs
add = input("give an initial value for the list: ")
my_list = []
user_input = 'y'
#defining the function
def append_to_list(add, user_input):
    while user_input.lower() == 'y': #while loop to keep asking the user if they want to add more values
        my_list.append(add) #appending the value to the list
        user_input = input("do you want to add another value to the list? (y/n): ") #asking the user if they want to add another value
        if user_input.lower() == 'y': #if they say yes, ask for another value
            add = input("give a value to add to the list: ")
        else: #if they say no, break the loop and print the created list
            print("here is your list: ", my_list)
    return my_list

append_to_list(add, user_input)