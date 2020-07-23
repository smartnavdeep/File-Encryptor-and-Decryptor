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

    try:

        keyfile = open('key.txt','rb')
        key = keyfile.read()
        keyfile.close()

        filename = input(r"File to Encrypt : ")
        with open(filename,'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)


        with open(filename,'wb') as f:
            f.write(encrypted)

        print("""File Encrypted successfully""")

    except:
        print('Oops! File not Found.')

def dec():

    try:

        keyfile = open('key.txt','rb')
        key = keyfile.read()
        keyfile.close()

        file_name = input("File to Decrypt : ")
        with open(file_name,'rb') as f:
            data = f.read()

        f2 = Fernet(key)
        decrypted = decrypted = f2.decrypt(data)

        with open(file_name,'wb') as fileD:
            fileD.write(decrypted)

        print("""File decrypted successfully.""")

    except:
        print('Oops! File not Found.')


# End of funtions
# Execution

generate_the_key()
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
