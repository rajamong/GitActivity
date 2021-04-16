import random

def generator(length):
    password = ""
    for x in range(length):
        letterType = random.randint(1,3)

        if(letterType == 1):
            char = random.randint(48,57)
            char = chr(char)
        elif(letterType == 2):
            char = random.randint(65,90)
            char = chr(char)
        else:
            char = random.randint(97,122)
            char = chr(char)

        password += char
    
    print("generated password: " + password)


length = int(input("enter your password length: "))
generator(length)