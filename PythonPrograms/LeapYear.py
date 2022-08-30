year = int(input("Enter the year to be calculated for leap or not\n"))
a=year%4
print(type(a))
print(a)

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("this is a leap year")
else:
    print("The given year is not leap year")

print("Calender Function running")
import calendar
print(calendar.isleap(year))

# Solution 3

print("Solution 3 is running")
n=year
def leapyr(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False
print(leapyr(n))