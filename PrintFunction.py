#this program will print a mesage function, then call a second message function
def print_message1():
    print("I was called first")
    print_message2()

def print_message2():
    print("I was called by print_message1")

print_message1()