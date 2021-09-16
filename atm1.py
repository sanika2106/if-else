# atm code

print("welcome to ATM!")
print("plz enter your ATM card!")

language=input("select your language:")
#language=English
if language=='english':
    print("select your transaction")
    transaction=input("enter the mode of transaction:")
    #mode=cash withdrawal
    if transaction=='cash withdrawal':
        print("plz enter the amount you want to withdraw")
        amount=int(input("enter the amount:"))
        #amounnt=1000
        if amount>=1000:
            print("plz select your account")
            account=input("enter your account type:")
            # account=saving
            if account=='saving':
                print("now plz enter your PIN")
                PIN=int(input("enter your 4 digit PIN:"))
                #PIN=1234
                if PIN==1234:
                    print("your transaction is in progress plz wait!")
                    print("kindly collect your amount and your card before moving!")
                else:
                    print("plz enter correct pin")
            else:
                print("plz select valid account type")
        else:
            print("plz enter amount within limit")
    else:
        print("plz select proper mode for transaction")
else:
    print("plz select language from given option!")


