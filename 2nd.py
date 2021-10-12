#leap year

# year=int(input("enter the number:"))
# if year%4==0:
#     print("its leap year")
#     year2=int(input("enter the number"))
#     if year2%400==0:
#         print("its also a leap year")
#     else:
#         print("its not leap year")
# else:
    # print("its also not a leap year")


year=int(input("enter the year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print("its leap year")
    # year2=int(input("enter the year:"))
    # if year%100!=0:
    #     print("its also leap year")
    # else:
        # print("no its not leap year")
else:
    print("sorry its not leap year")