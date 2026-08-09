#password generator 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the Password Generator!")
letters1 =int(input("how many letters you want in password : "))
symbols1 =int(input("how many symbols you want in password : "))
numbers1 =int(input("how many numbers you want in password : "))

password=[]

for l in range(0,letters1):
    randomletter=random.choice(letters)
    password.append(randomletter)
for s in range(0,symbols1):
    randomsymbol=random.choice(symbols)
    password.append(randomsymbol)
for n in range(0,numbers1):
    randomnumber=random.choice(numbers)
    password.append(randomnumber)
random.shuffle(password)
orig_pass=""
for i in password:
    orig_pass+=i
print(f"your password is {orig_pass}")