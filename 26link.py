# A company decided to give a bonus of 5% to an employee if his/her year of service is 
# more than 5 years. Ask users for their salary and year of service and print the net bonus amount.


salary=int(input("enter the salary:"))
service=int(input("enter the total year of srevice:"))
if service>5:
    bonus=5/100*salary
    print("your net bonous",bonus)
else:
    print("your net bonous can not generated because year of service is less than 5 year")

