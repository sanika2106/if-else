#prime number

num=int(input("enter the number:"))
if num%2!=0 and num%3!=0 and num%5!=0:
    print("prime number")
    # num2=int(input("enter the number:"))
elif num==2 or num==3 or num==5:
     print("it is also a prime number")
else:
    print("not a prime number")





