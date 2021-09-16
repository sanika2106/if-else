#prime number

num=int(input("enter the number:"))
if num%2!=0:
    print("prime number")
    num2=int(input("enter the number:"))
    if num2==2:
        print("it is also a prime number")
    else:
        print("it is not a prime number")
else:
    print("not a prime number")