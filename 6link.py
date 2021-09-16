#check whether a year is leap or not 


# year=int(input("enter the number"))
# if year%4==0 :
#     print ("leap year")
# elif year%400==0:
#     print("it is also leaf year")
# else:
#     print("not leap year")


year =int(input("enter the number"))
if year%4==0 and year%100!=0 or year%400==0:
    print("leap year")
else:
    print("not leap year")