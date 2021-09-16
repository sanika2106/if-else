# find the current age 

birth_year=int (input("enter the birth year:"))
current_year=int(input("enter the current year:"))
current_age= current_year-birth_year
if current_year -birth_year>0:
    print("your current age is",current_age)
elif current_year-birth_year<1:
    print("child age is less than 1 year")
else:
    print("error")
    