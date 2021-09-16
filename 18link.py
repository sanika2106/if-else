# write c program to input marks of 5 subjects phy,chem,bio,math,comp. calculate percentage 
# and gradeaccording to following
# per>=90%:grade A
# per>=80%:grade B 
# per>=70%:grade C 
# per>=60%:grade D 
# per>=40%:grade E 
# per<=40%:grade F 


phy=int(input("enter the number:"))
chem=int(input("enter the number:"))
bio=int(input("enter the number:"))
math =int(input("enter the number:"))
comp=int(input("enter the number:"))

per=(phy+chem+bio+math+comp)/500*100
if(per>=90):
    print("grade A")
elif(per>=80):
    print("grade B")
elif(per>=70):
    print("grade C")
elif(per>=60):
    print("grade D")
elif(per>=40):
    print("grade E")
else:
    print("grade F")

