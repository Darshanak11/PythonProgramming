#leap year program
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input("Enter the year: "))
if leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")