# This program can create random passwd

#---------  Start import
import random


#--------- Start program
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!$%&*()-_"
num = 0


# Ask start program
start = input("Do you want to start program? [Y/n]")
if start=="y" or start=="Y":
    while True:
        print(' ')
        passwd_len = int(input("What length would you like your password to be :"))
        passwd_count = int(input("How many passwords would you want to create :"))


        print("")
        print("---- Passwords ----")

        #-------- Start create passwd
        for x in range(0,passwd_count):
            passwd = ""
            for x in range(0,passwd_len):
                passwd_char = random.choice(chars)
                passwd = passwd + passwd_char
            print("Here is your password : ", passwd)
        print("-------------------")
        print("")
        keep = input("Do you want to create password again? [Y/n]")
        if keep=="Y" or keep=="y":
            author = "John"
        else:
            print("")
            print("Done.......")
            break
else:
    print("Done....")
