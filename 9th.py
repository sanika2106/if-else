# Accept the number of days from the user and calculate the charge for library according to following :
# First five days : Rs 2/day.
# Six to ten days  : Rs 3/day.
# Ten to 15 days  : Rs 4/day
# After 15 days    : Rs 5/day


days=int(input("enter the number:"))
charge1=days*2
charge2=days*3+charge1
charge3=days*4+charge2
charge4=days*5+charge3
if 0>=5:
    print("totalcharge",charge1)
elif 6>=10:
    print("total charge",charge2)
elif 10>=15:    
    print("total charge",charge3)
else:
    print("total charge",charge4)