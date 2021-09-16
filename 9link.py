# check whether it is alphabet number or special characters


ch=input("enter the number")
if ((ch>='a' and ch<='z')):
    print("this is alphabet")
elif (ch>='0' and ch<='9'):
    print("this is number")
else:
    print("this is special character")


