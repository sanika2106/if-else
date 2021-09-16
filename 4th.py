#Write a program to find the lowest number out of two numbers excepted from the user.

# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# if num1>num2:
#     print("num2 is lowest num")
# elif  num1==num2:
#     print("both num1 and num2 are equal")  
# else:
#     print("num1 is lowest number")

num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num3=int(input("enter the number:"))
if num1<num2 and num1<num3:
    print("num1 is lowest")
elif num2<num1 and num2<num3:
    print("num2 is lowest") 
elif num3<num1 and num3<num2:
    print("num3 is lowest")
else:
    print("wrong")


