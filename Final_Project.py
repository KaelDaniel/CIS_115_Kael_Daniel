#the final Project

def Print_box(): #defined the function that holds the product catalog
    print("        ---------------------------------------------------------------")
    print("	                           PRODUCT CATALOG                     ")
    print("	---------------------------------------------------------------")
    print("	1      |    USB Drive(128 GB)                           |   $12.00")
    print("	2      |   Mac Book Pro(15 inch)                    |   $2900.00")
    print("	3      |   Arduino 1010(with blue tooth)     |   $48.00")
    print("	4      |   Ring Camera(wireless)                    |   $156.00")
    print("	5      |   Smart TV(TCL 70 inch)                     |   $359.00")
    print("	----------------------------------------------------------------")

Product_Catalog = {
"1":12.00, 
"2":2900.00, 
"3":48.00, 
"4":156.00, 
"5":359.00, 
} #dictionary that holds the product id number with prices

Print_box() #call the function to print the product catalog as the start of the program

Shopping_cart = {} #empty dictionary to hold the shopping cart items

def Users_information(): #mostly a place holder for now. (will update later)
    User_info = {
        "first name":v,
        "last name":w,
        "address":x,
        "city":y,
        "state":z,
        "zip/post code":a,
        "email":b,
        "phone":c,}
    print("Please enter your personal information:")
    v = input("First Name: ")
    w = input("Last Name: ")
    x = input("Address: ")
    y = input("City: ")
    z = input("State: ")
    a = input("Zip/Post Code: ")
    b = input("Email: ")
    c = input("Phone: ")

def shopping_cart_function(): #function that allows user to add items to shopping cart. (might change in the future, but works for now)
    while True:
        item_id = input("Enter the product ID number to add to your shopping cart your desired product. (or type 'done' to finish): ")
        if item_id.lower() == 'done':
            break
        elif item_id in Product_Catalog:
            quantity = int(input("Please enter your required quantity: "))
            if item_id in Shopping_cart:
                Shopping_cart[item_id] += quantity
            else:
                Shopping_cart[item_id] = quantity
            print(f"Added {quantity} of item ID'd as {item_id} to your shopping cart.")
        else:
            print("Invalid product ID. Please try again.")

CCN = int(input("Please enter your credit card number: "))

def credit_card_verify(credit): #function to verify credit card information
    credit_list = str(credit) #converting credit card number to a string
    reverse = credit_list[::-1] #reversing the string

    sum1 = 0 #doubled
    sum2 = 0 #same

    for num in range(len(reverse)): 
        number = int(reverse[num]) 
        if num % 2 == 1: 
            number *= 2 
            if number > 9: 
                number -= 9
            sum1 += number
        else:
            sum2 += number
    total = sum1 + sum2
    if total % 10 == 0:
        print(f"The credit card number {credit} is valid.")
    else:
        credit = int(input("Invalid credit card number. Please try again: "))
if len(str(CCN)) < 13 or len(str(CCN)) > 16:
    print("Invalid credit card number length.")
else: 
    credit_card_verify(CCN) #function to verify credit card information (testing phase)