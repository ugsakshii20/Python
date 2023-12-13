def is_leap_year(year):
    if year % 400==0:
        print("Year is leap year")
    elif year % 4 ==0 and year % 100 !=0:
        print("Year is leap")
    else:
        print("Year is not leap")

year=int(input("Enter the year"))

print(is_leap_year(year))
