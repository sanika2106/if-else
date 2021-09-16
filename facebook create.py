#facebook account create

# print("welcome to facebook")
# name=input("enter the name:")
# # name="Sanika Tidake"
# if name== 'sanika tidake' :
#     print("next step")
#     birthdate=input("enter the birthdate:")
#     # birthdate=21/6/2002
#     if birthdate=="21/6/2002":
#         print("next step")
#         gender=input("enter the gender:")
#         # gender= 'female'
#         if gender=='female':
#             print("next step")
#             mobile=int(input("enter the mobile number:"))
#             # mobile=7350471140
#             if mobile==7350471140:
#                 print("next step")
#                 password=input("enter the password:")
#                 # password='sanika@123'
                # if password=='sanika@123':
                #     print("facebook account succesfully created ")
                # else:
                #     print("fogot password!")
                #     mobile=int(input("enter the mobile number:"))
                #     #mobile=7350471140
                #     if mobile==7350471140:
                #       print ("plz enter the otp you receive in your mobile") 
                #       opt=int(input("enter the otp:")) 
                #       #opt=1234
                #       if opt==1234:
                #           print("enter new password")
                #           password=int(input("enter the new password:"))
                #           #password=12345678
                #           if password==12345678:
                #               print("new password successfully created!")
                #           else:
#                               print("error")
#                       else:
#                         print("plz enter correct otp")
#                     else:
#                         print("enter correct mobile number")
#             else:
#                print("enter valid mobile num")
#         else:
#             print("plz enter correct gender")
#     else:
#         print("plz enter correct birthdate")
# else:
#     print("wrong name")



print("welcome to facebook")
name=str(input("enter the name:"))
if name>='a'and name<='z':
    print("next step")
    birthdate=input("enter the birthdate:")
    if birthdate>=0 and birthdate<=9:
        print("next step")
        gender=input("enter the gender:")
        if gender== "male" or "female":
            print("next step")
            mobile=int(input("enter the mobile number:"))
            if mobile>=0 and mobile<=9:
                print("next step")
                password=input("enter the password:")
                if password>="a" and password<="z"and password>="A" and password>="z"and password>=0 and password<=9:
                    print("facebook account succesfully created ")
                else:
                    print("wrong password")
            else:
               print("enter valid mobile num")
        else:
            print("plz enter correct gender")
    else:
        print("plz enter correct birthdate")
else:
    print("wrong name")




     

     
