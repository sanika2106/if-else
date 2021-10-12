# last digit ends with 4\ divisible by 4

number=int(input("enter the number:"))
modulus=number%10
if modulus%4==0:
    print(modulus,"divisible by 4")
else:
    print(modulus,"not divisible by 4")



