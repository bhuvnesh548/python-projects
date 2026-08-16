from getpass import getpass
import pwinput
def create_account(name,mobile,address):
    info=[name,mobile,address]
    for i in info:
        with open("info.csv","a")as f:
            f.write(str(i) + ",")
def credit(number,amt,passw):
    pass
def debit(number,amt):
    pass
def view(number,amt):
    pass

print(f"{"| Money Machine |":~^50}")
option=input("select a option : 1.credit/2.debit/3.view statement/4.create Account")
if option=="1":
    account= 1234567890#int(input("enter the account number: "))
    amount= 1000#int(input("enter amount: "))
    password = 12345 #pwinput.pwinput(prompt='Enter password: ', mask='⁕')
elif option=="2":
    account=1234567890
    amount=1000
elif option=="3":
    account=1234567890
    password=12345
elif option=="4":
    name="bhuvnesh"
    mobile=1234567890
    address="bareilly"
    create_account(name,mobile,address)
else:
    print("select a valid option !")