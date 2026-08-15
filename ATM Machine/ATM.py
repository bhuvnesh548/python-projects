from getpass import getpass
import pwinput

def credit(number,amt,passw):
    pass
def debit(number,amt):
    pass
def view(number,amt):
    pass

print(f"{"| welcome to Bank of Ghotala ATM |":~^50}")
account=int(input("enter the account number: "))
amount=int(input("enter amount: "))
password = pwinput.pwinput(prompt='Enter password: ', mask='⁕')