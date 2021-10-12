# c program to input month number and print number of days in that month

month=input("enter the month:")
if(month=='january' or month=='march' or month=='may' or month=='july' or month=='august' or month=='octommber' or month=='december'):
   print("31 days")
elif(month=='april'or month=='june' or month=='september' or month=='november'):
    print("30 days")
elif(month=='february'):
    print("28 or 29 days")
else:
    print("error! enter the correct month")

