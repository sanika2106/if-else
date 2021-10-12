#Accept the temperature in degree Celsius of water and check whether it is boiling or
#  not (boiling point of water in 100 oC.

tempoC= int(input("enter the number:"))
if tempoC>100 or tempoC==100:
    print("boiling")
    # tempoC2=int(input("enter the number:"))
    # if tempoC2==100:
    #     print("its also boiling")
    # else:
        # print("its not boiling")
else:
    print("not boiling")

