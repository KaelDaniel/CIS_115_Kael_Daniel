#this program will return the months that would be between an inputted start month and end month


def month_of_year(startMonth,endMonth):
    months=["jan","feb","march","april","may","june","july","august","sept","oct","nov","dec"]
    return months[startMonth:endMonth]

start = int(input("Enter the start month (only a number from 0 to 11): "))
end = int(input("Enter the end month (only a number from 1 to 12): "))

print(month_of_year(start,end))