# A shop will give a discount of 10% if the cost of the purchased quantity 
# is more than 1000. Ask the user for quantity, Suppose, one unit will cost 100. 
# Judge and print total cost for user

quanty=int(input("enter the number:"))
cost=100
totalcost=quanty*cost
totalcost1=totalcost-0.1*totalcost
if totalcost>1000:
    print("total cost with discount",totalcost1)
else:
    print("total cost without discount",totalcost)






