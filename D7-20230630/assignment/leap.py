leap_year=input("Enter the year:")
# print(type(leap_year))
leap_year=int(leap_year)
# print(type(leap_year))
is_checking=leap_year%4==0 and  leap_year%100!=0 or leap_year%400==0
if is_checking: 
    print(leap_year,"It is  a leap year")
else:
    print(leap_year,"It`s not a leap year")
