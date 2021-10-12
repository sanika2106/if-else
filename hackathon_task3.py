#check wether it is alphabet number or special character:

ch=input("enter number:")
if ch>='a'and ch<='z' or ch>="A" and ch<="Z":
    print("alphabet")
elif ch>='0' and ch<='9':
    print("number")
else:
    print("special character")