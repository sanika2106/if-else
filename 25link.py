# Write a python program to input basic salary of an employee and calculate its 
# Gross salary according to following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%


basic_salary=int(input("enter the salary:"))
if(basic_salary<=10000):
   HRA=20/basic_salary*100
   DA=80/basic_salary*100
   gross_salary= basic_salary +HRA+DA
   print("employee salaryis >=10000",(gross_salary))
elif (basic_salary<=20000):
   HRA=25/basic_salary*100
   DA=90/basic_salary*100
   gross_salary=basic_salary+HRA+DA
   print("employee salary >20000",(gross_salary))
elif(basic_salary>20000):
   HRA=30/basic_salary*100
   DA=95/basic_salary*100
   gross_salary=basic_salary+HRA+DA
   print("employee salary",(gross_salary))
else:
   print("enter the correct amount")




   

 

# a=input("enter the name")
# b=input("enter the name")
# print(b+a)





 