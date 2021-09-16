#last digit ends with 3 divisible by 3

number=int(input("enter the number:"))
if number%10==3:
    print("divisible by 3")
    number2=int(input("enter the number:"))
    if number2%3==0:
        print("divisible")
    else:
        print(" not divisible")
else:
    print("not divisible by 3")