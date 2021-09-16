 #Write a program to check whether a person is a senior citizen or not.


age=int(input("enter the age:"))
if age==60:
    print("senior citizon")
    age2=int(input("enter the age2:"))
    if age2>=60:
        print("yes it is also a senior citizon")
    else:
        print("it is not a senior citizen")
else:
    print("not a senior citizen")

