#Write a program to check whether a number entered is a three digit number or not.

num=int(input("enter the number:"))
if num>99 and num<=999:
    print("three digit number")
    # num2=int(input("enter the number:"))
    # if num2<=999:
    #     print("it is also a three digit number")
    # else:
    #     print("it is not three digit number")
else:
    print("not three digit number")