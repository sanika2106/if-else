print("welcome to ATM")
print("plz enter your card")
import time
time.sleep(5)
# pin=1234
pin=int(input("enter your pin:"))
if pin==1234:
    print("plz select your language")
    # language='hindi'or 'english'
    language=input("enter your language:")
    if language=='hindi' or 'english':
        print("select your account type")
        # account_type='saving'or 'current'
        account_type=input("enter the account type:")
        if account_type=='saving'or 'current':
          print("plz select transaction type")
        #   transaction_type= 'withdrawal' or 'deposit'or'change pin'
          transaction_type=input("enter the transaction type:")
          if transaction_type=='withdrawal' or 'deposit' or 'change pin':
              print("plz enter the amount you want to withdrawal")
            #   amount=10000
            #   amount=int(input("enter the amount:"))
            #   if amount<=10000:
                #   print("your transaction is in progress plz wait") 
              withdrawal=int(input("enter withdrawal amount:"))
              balance=10000-withdrawal
              if withdrawal-10000:
                  print("your balance amount",balance)
              else:
                  print("wrong amount")
          else:
            print("enter the amount within limit")
        else:
            print("plz select valid transaction type")
    else:
        print("plz select correct account type")
else:
    print("change pin")
    new_pin=3456
    new_Pin=int(input("enter the new pin:"))
    if new_pin==3456:
        print("your new pin is generated successfully")
    else:
        print("plz enter strong pin!")


                



