#the final Project

def Print_box(): #defined the function that holds the product catalog
    print("        ---------------------------------------------------------------")
    print("	                           PRODUCT CATALOG                     ")
    print("	---------------------------------------------------------------")
    print("	1      |    USB Drive(128 GB)                        |   $12.00")
    print("	2      |   Mac Book Pro(15 inch)                     | $2900.00")
    print("	3      |   Arduino 1010(with blue tooth)             |   $48.00")
    print("	4      |   Ring Camera(wireless)                     |  $156.00")
    print("	5      |   Smart TV(TCL 70 inch)                     |  $359.00")
    print("	----------------------------------------------------------------")

Product_Catalog = {
"1":(12.00, "usb_k981", " USB 128 GB drive.", 1000), 
"2":(2900.00, "mbpro_490", "Mac Book Pro 15 inch.", 45),
"3":(48.00, "chip_1010", "Arduino microprocessor", 325),
"4":(156.00, "cam_78", "Ring Camera. Model 78.", 98),
"5":(359.00, "smt_tv_100", "TCL Smart TV.", 225)
} #dictionary that uses the product id as the key holding the rest of the info

qty = [Product_Catalog[item][3] for item in Product_Catalog]
#line 22 is meant to help seperate the product quatity from the user inputed quantity

Shopping_cart = {} #empty dictionary to hold the shopping cart items


def shopping_cart_function(): #function that allows user to add items to shopping cart. (might change in the future, but works for now)
    while True:
        item_id = input("Enter the product ID number to add to your shopping cart your desired product. (or type 'done' to finish): ") #asks user for what they want
        if item_id.lower() == 'done': #if they choose to type done then they will end the proccess 
            break
        elif item_id in Product_Catalog:
            quantity = int(input("Please enter your required quantity: ")) #after the id is how much of the item
            if item_id in Shopping_cart: #and this part is what adds to the quantity if there is already some of the chosen item in the cart
                Shopping_cart[item_id] += quantity
            else:
                Shopping_cart[item_id] = quantity #adds the item and quantity
            print(f"Added {quantity} of item ID'd as {item_id} to your shopping cart.")
            if quantity > Product_Catalog[item_id][3]: #checking if the quantity requested is more than the stock available
                print("Warning: Requested quantity exceeds available stock, please adjust your order.")
                print(f"Warning: Only {Product_Catalog[item_id][3]} items are in stock.") #if so, warn the user
        else:
            print("Invalid product ID. Please try again.") #if something was incorrect, then cycle/loop

Print_box() #call the function to print the product catalog as the start of the program

shopping_cart_function() #calling the shopping cart function

CCN = int(input("Please enter your credit card number: ")) #credit card input

def credit_card_verify(credit): #function to verify credit card information
    credit_list = str(credit) #converting credit card number to a string
    reverse = credit_list[::-1] #reversing the string

    sum1 = 0 #doubled
    sum2 = 0 #same

    for num in range(len(reverse)): #iterating through each digit in the reversed credit card number
        number = int(reverse[num]) #converting each character back to integer for calculation
        if num % 2 == 1: 
            number *= 2 
            if number > 9: 
                number -= 9
            sum1 += number
        else:
            sum2 += number
    total = sum1 + sum2
    return total


if len(str(CCN)) < 13 or len(str(CCN)) > 19: #checking the length of credit card number
    print("Invalid credit card number length.")
else: 
    credit_card_verify(CCN) #function to verify credit card information (testing phase)
    cycle = False
    while cycle == False:
        cycle = credit_card_verify(CCN)
        if cycle % 10 == 0: #checking if the total modulo 10 is 0
            print("please enter the card's expiration date and your personal information.") 
            exp_date = input("Expiration Date (MM/YY): ") #user inputs for user information
            v = input("First Name: ")
            w = input("Last Name: ")
            x = input("Address: ")
            y = input("City: ")
            z = input("State: ")
            a = input("Zip/Post Code: ")
            b = input("Email: ")
            c = input("Phone: ")
            cycle = True
        else:
            cycle = False 
            CCN = int(input("Invalid credit card number. Please try again: ")) #prompting user to re-enter credit card number if the card was wrong, until a valid card is entered

def billing_and_shipping_and_cart(y): #function to generate receipt
    print("----------------------------------------------------------------------------------------")
    print("                                            Billing/Shipping Information:")
    print("----------------------------------------------------------------------------------------")
    print(f"{v} {w}") #printing the billing and shipping information
    print(f"Adress: {x}")
    print(f"City: {y}")
    print(f"State: {z}")
    print(f"Zip/Post Code: {a}")
    print(f"Email: {b}")
    print(f"Phone: {c}")
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("                                               Shopping Cart Information:")
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("****************************************************************************************************************************")
    print("                SKU             Qty          Price                      Description                                 Total")
    print("****************************************************************************************************************************")
    cart_total = 0 #variable to hold the cart total
    for item_id, quantity in Shopping_cart.items(): #iterating through each item in the shopping cart
        price, sku, description, y, = Product_Catalog[item_id] #getting the product details from the catalog
        total_price = price * quantity #calculating the total price for each item based on quantity
        cart_total += total_price #adding to the cart total
        print(f"                {sku}          {quantity}       ${price:.2f}               {description}               ${total_price:.2f}") #printing each item in the cart with its details
    print("*****************************************************************************************************************************")
    print(f"            cart Total: ${cart_total:.2f}") #printing the cart total at the end of the receipt

billing_and_shipping_and_cart(qty) #calling the function to generate receipt