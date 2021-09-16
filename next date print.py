# Write a Python program to get next day of a given date.
# Expected Output:
# Input a year: 2016                                                      
# Input a month [1-12]: 08                                                
# Input a day [1-31]: 23                                                  
# The next date is [yyyy-mm-dd] 2016-8-24  

date=int(input("enter the date:"))
if date>=1 and date<=31:
    print("now enter the month")
    month=int(input("enter the month:"))
    if month>=1 and month<=12:
        print("plz enter the year now")
        year=int(input("enter the year:"))
        if year>=0 and year<=2021:
            print(date+1,"/",month,"/",year)
        else:
            print("plz enter valid year")
    else:
        print("plz enter the valid month")
else:
     print("plz enter valid date")


    

