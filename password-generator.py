import random

print("Your password: ")

#Available Characters for random password
chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?'

#make sure to leave password blank so it can generate.
password = ''
for x in range(10): #Use any number, make a long ass password for your complicated login. Then forget it. ;]
    password += random.choice(chars)

print(password)