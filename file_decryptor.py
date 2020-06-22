from cryptography.fernet import Fernet
import sys
import os
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
file_name = input("Enter the file name which must be decrypted :")
with open(file_name,'rb') as f:
    data = f.read()

f2 = Fernet(key)
decrypted = decrypted = f2.decrypt(data)
file_to = input("Enter the file name you want after decryption :")
with open(file_to,'wb') as fileD:
    fileD.write(decrypted)

print("""File decrypted
{0} - {1}
Decryption completed
""".format(file_name,file_to))

sleep(0.5)

input("To avoid confusion between the encrypted and decrpyted, please press enter to delete the encrypted file. ")
sleep(1)

os.remove(file_name)
print("File removed successfully")
sleep(2)
