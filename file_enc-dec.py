# Start
from cryptography.fernet import Fernet
from time import sleep
import sys
# Some info
passnum=692008
key = Fernet.generate_key()
error1,error2="""File not found!""","""Error: Tried open Binary"""
# Functions
def verification():
    try:
        passcode=int(input('Enter your Passcode:').replace(' ',''))
        if passcode==passnum:
            print('Access granted.')
        else:
            print('Access denied!')
    except ValueError:
        print('Pascode is not any number, passcode must be an interger.')


def enc():

    try:

        filename = input(r"File to Encrypt : ")
        with open(filename,'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)


        with open(filename,'wb') as f:
            f.write(encrypted)

        print("""File Encrypted successfully""")
        sleep(0.5)
    except FileNotFoundError:
        print(error1)

def dec():

    try:

        file_name = input("File to Decrypt : ")
        with open(file_name,'rb') as f:
            data = f.read()

        f2 = Fernet(key)
        decrypted = decrypted = f2.decrypt(data)

        with open(file_name,'wb') as fileD:
            fileD.write(decrypted)

        print("""File decrypted successfully.""")
        sleep(0.5)    
    except FileNotFoundError:
        print(error1)


# End of funtions
# Execution

print("Hello my name is Enc and Dec.")
sleep(0.5)
print('')

while True:
    mode=input('What do you want to run: Encryption or Decryption : ').lower().replace(" ", "")
    mode=mode[0:3]
    print('')

    if mode=='enc':
        print('Ok')
        print('')
        enc()
    elif mode=='dec':
        print('Ok')
        print('')
        dec()
    else:
        print('Correct Method not choosen !')

# End
