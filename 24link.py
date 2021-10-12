# A student will not be allowed to sit in an exam if his/her attendance is less 
# than 75%.Take following input from the user. Number of classes held. Number of 
# classes attended. And print, percentage of class attended. Is the student is 
# allowed to sit in the exam or not.

num1=int(input("enter the number of classes held:"))
num2=int(input("enter the number of classes not attended:"))
totalattendence=num1-num2
total_attendence_percentage=totalattendence/num1*100
if total_attendence_percentage>=75:
    print("student allowed to sit in exam and present percentage are",total_attendence_percentage)
else:
    print("student not allowed to sit in exam and present percentage are",total_attendence_percentage)
