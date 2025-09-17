#this code will calculate the tax on a purchase

sales_tax = .0725
price = float(input("Enter the price of the item: "))
tax = price * sales_tax
total = price + tax
print("The tax is: $", format(tax, ",.2f"), sep="")
print(", and the total is: $", format(total, ",.2f"), sep="")