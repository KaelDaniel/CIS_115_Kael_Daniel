#this program will prompt the user to slice a string
#and display the sliced string

slice_value= (input("Enter a string to slice: "))

def slice_my_string(slice):
    valv=slice[0:3]
    return valv

print(slice_my_string(slice_value))