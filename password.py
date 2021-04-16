import random

def generatePassword(length):
    password = ['a'] * length
    for i in range(0, length):
        password[i] = chr(random.randint(32, 126))
        print(password[i], end = '')

num = 0
while(1):
    try:
        num = int(input("Enter the password length: "))
        break
    except:
        print("Invalid input")