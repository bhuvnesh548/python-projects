#ceaser cypher
# This program implements a simple Caesar cipher encryption and decryption.
# message =input("enter a message : ")
# shift =int(input("enter shift : "))
# letters ="abcdefghijklmnopqrstuvwxyz"
operation=input("type encode or decode : ").lower()
if operation=="encode":
    message =input("enter a message : ")
    shift =int(input("enter shift : "))
    letters ="abcdefghijklmnopqrstuvwxyz"
    encrypted_message =""
    for i in message.lower():
        if i in letters:
            index =letters.index(i)
            new_index =(index + shift) % 26
            encrypted_message +=letters[new_index]
    print("Encrypted message:",encrypted_message)
else: 
    message =input("enter a message : ")
    shift =int(input("enter shift : "))
    letters ="abcdefghijklmnopqrstuvwxyz"
    decrypted_message=""
    for i in message.lower():
        if i in letters:
            index=letters.index(i)
            new_index =(index - shift) % 26
            decrypted_message +=letters[new_index]
    print("decrypted message:",decrypted_message)
