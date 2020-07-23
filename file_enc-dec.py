# Start
from cryptography.fernet import Fernet
from time import sleep 
# Functions

def generate_the_key():

    key = Fernet.generate_key()

    file = open("key.txt","wb")
    file.write(key)
    file.close()

def enc():
    pass

def dec():
    pass

# End of funtions
# Execution
print("Hello my name is Enc and Dec.")
sleep(0.5)
print('')

mode=input('What do you want ot run: Encryption or Decryption : ').lower().replace(" ", "")
mode=mode[0:3]
print('')

if mode=='enc':
    print('Ok')


if mode=='dec':
    print('Ok')

else:
    print('Correct Method not choosen !')

# End
