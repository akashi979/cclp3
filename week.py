import datetime
year=int(input("Enter year: "))
month=int(input("Enter month: "))
day=int(input("Enter day: "))
print("week number: ",datetime.date(year, month, day).isocalendar()[1])
