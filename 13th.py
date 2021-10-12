#last digit ends with 3 divisible by 3

number=int(input("enter the number:"))
modulus=number%10
if modulus%3==0:
    print(modulus,"divisible by 3")
else:
    print(modulus,"not divisible by 3")



