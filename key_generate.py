from cryptography.fernet import Fernet
from time import sleep

key = Fernet.generate_key()
print(key)

sleep(1)

# NEW FILE
file = open("key.txt","wb")
file.write(key)
file.close()
# Key written
# End
