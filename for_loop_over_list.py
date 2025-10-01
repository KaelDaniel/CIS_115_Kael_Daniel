#this program will print out a list of items using a for loop
list = [10,20,30,40,50,60]

def getMylist(list):
    for item in list:
        print(item)

getMylist(list)
print(f"The length of the list is: {len(list)}")