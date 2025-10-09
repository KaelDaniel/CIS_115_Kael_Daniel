#this program will find a month from a list by their input


month_input=input("Enter a month (abbreviated to 3 letters): ")

def search(month):
    months=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
    if month in months:
        return f"{month} is in the list"
    else:
        return f"{month} is not in the list"

print(search(month_input))