#To find whether a given year is a leap year
year =int(input("Enter the year:"))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("Is a leap year")
else:
    print("Is not a leap year")