num = float(input("please enter a number: "))
print("your divisors are:")
divider = 1

while divider <= num :
    if (num % divider==0) :
        print(divider),
    divider = divider + 1
