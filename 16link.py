# c program to check weather the triangle is equilateral ,isosceles or scalene triangle

side1=int(input("enter the number:"))
side2=int(input("enter the number:"))
side3=int(input("enter the number:"))
if(side1==side2 and side2==side3 and side1==side3):
    print("it's a equilateral triangle")
elif(side1==side2 or side2==side3 or side1==side3):
    print("it's a isosceles triangle")
else:
    print("it's a scalene triangle")