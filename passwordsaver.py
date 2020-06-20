# Don't Blame me if some one stole your passwords
# I will find a solution to encrypt the data
# Other information
from time import sleep
import sys

p = "692008"
print("PASSWORD KNOWN!")
print()
pc = input("Enter the Passcode :")
# End of other information

# Start
# Data
data1 = """"""
data2 = """"""
data3 = """"""
data4 = """"""
data5 = """"""
data6 = """"""
# End of Data


# Functions
def no_access():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>Verifying User<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    sleep(0.5)
    print("Access denied")
    sleep(0.5)
    print(".......................................................................")
    sys.exit()


def access():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>Verifying User<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    sleep(0.5)
    print("Access Granted")
    sleep(1)
    print("Passwords Available")
    print("""
    Data1
    Data2
    Data3
    Data4
    Data5
    Data6
          """)

    def iwant():
        while True:
            try:
                want = input("Which Password do you want: ")
                want = eval(want)
                print(want)
            except NameError:
                print("Sorry Password not available")
    iwant()

# End of Functions
if pc == p:
    user = input("What is your User name?: ")
    if user == "username":
        access()
    else:
        no_access()
else:
    no_access()
# End

# By Navdeep