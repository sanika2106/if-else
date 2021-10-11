#prime number
num=int(input("enter the number:"))
if num==1 or num==0:
    print("not a prime number")
elif num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0:
    print("prime number")
elif num==2 or num==3 or num==5 or num==7 :
    print("it is also a prime number")
else:
    print("not a prime number")  
