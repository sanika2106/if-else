# c program to input month number and print number of days in that month

month=int(input("enter the month:"))
if (month==1):
    print("january 31days")
elif (month==2):
    print("february 28 or 29 days")
elif (month==3):
    print("march 31 days")
elif (month==4):
    print("april 30 days")
elif (month==5):
    print("may 31 days")
elif (month==6):
    print("june 30 days")
elif (month==7):
    print("july 31 days")
elif (month==8):
    print("august 31 days")
elif (month==9):
    print("september 30 days")
elif (month==10):
    print("octomber 31 days")
elif (month==11):
    print("november 30 days")
elif (month==12):
    print("december 31 days")
else:
    print("error! enter correct month number")