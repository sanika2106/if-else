age=int(input("enter the number"))
if age>=5 and age<=18:
    print("can go to school")
elif age>=18 and age<=21:
    print("""1.can go to school,
           2.can vote in election""")
elif age>=21 and age<=24:
    print("""1.can go to school,
        2.can vote in election,
        3.can drive a car""")
elif age >=24 and age<=25:
    print("""1.can go to school,
          2.can vote in election,
          3.can drive a car,
          4.can marry""")
elif age >25:
    print("""1.can go to school,
         2.can vote in election,
         3.can drive a car,
         4.can marry,
         5.can legally drink""")
else:
    print("can not legally drink")