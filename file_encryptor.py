from cryptography.fernet import Fernet
import os
import sys
from time import sleep
# access
passcode = "692008"

password = input("Enter the password :")

if password == passcode:
    print("Access granted !")
    sleep(1)
else:
    print("Access denied !")
    sleep(1)
    sys.exit()

keyfile = open('key.txt','rb')
key = keyfile.read()
keyfile.close()

filename = input("File to Encrypt : ")
with open(filename,'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)
file_to = input("File name after encryption :")

with open(file_to,'wb') as f:
    f.write(encrypted)

print("""File Encrypted successfully
{0} - {1}
""".format(filename,file_to))

dele = input("For safety reasons do you want to delete the original file ?").replace("es", "").replace("o", "")
if dele == "y":
    print("Ok")
    try:
        confirm = input("Please enter the file path/name to confirm :")
        os.remove(confirm)
        print("File removed successfully")
        sleep(1)
    except NameError:
        print("Error: File not found!")
        print("Try again!")
        sleep(1)
