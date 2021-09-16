# Write a python program to input electricity unit charges and calculate total electricity bill 
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

electricity_unit=int(input("enter the unit:"))
total_charge1=electricity_unit*0.50
total_charge2=electricity_unit* 0.75 + total_charge1 
total_charge3=electricity_unit*1.20+total_charge2
total_charge4=electricity_unit*1.50+total_charge3
if 0<=50:
     print("electricity_unit charges",total_charge1)
elif 50<=100:
     print("electricity_unit charge",total_charge2)
elif 100<=200:
     print("elctricity unit charge",total_charge3) 
elif 200<=250:
     print("electricity unit charge",total_charge4)
else:
     print("enter the correct electricity_unit")

     







