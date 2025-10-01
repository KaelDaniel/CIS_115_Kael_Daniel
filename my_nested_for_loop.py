#this program demonstrates a nested for loop

list1 = [1,2,3]

list2 = ['card1','card2','card3']

for item1 in list1:
    for item2 in list2:
        print(f"draw{item1}, {item2}")
    print("possible draws completed")