# Start

from cryptography.fernet import Fernet
import os
import sys
from time import sleep
# Funcy Funtions

# Key written
def genrate():
    key = Fernet.generate_key()

    sleep(1)

    # NEW FILE
    file = open("key.txt","wb")
    file.write(key)
    file.close()
# Key Over
# Encryption
def enc():
    filename = input("File to Encrypt : ")
    with open(filename,'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)


    with open(filename,'wb') as f:
        f.write(encrypted)

    print("""File Encrypted successfully.""")
    sleep(1)
# Decryption
def dec():

    file_name = input("Enter the file name which must be decrypted :")
    with open(file_name,'rb') as f:
        data = f.read()

    f2 = Fernet(key)
    decrypted = decrypted = f2.decrypt(data)
    with open(file_name,'wb') as fileD:
        fileD.write(decrypted)

    print("""File decrypted successfully.""")
# Ask Enc-Dec
while True:
    try:
        genrate()
        enc_dec = input("What do you want to run ? Encryption or Decryption.").lower().replace(" ", "")
        enc_dec = enc_dec[0:3]
        genrate()
        if enc_dec=='enc':
            
            enc()
            
        if enc_dec=='dec':
            
            dec()

        else:
            print('Error : Mode#not#choosen#correctly.')
    except:
        print('''Oops! Somthing went wrong !
        Please make sure that you weren't trying to decrypt a decrypted file.''')

# End
