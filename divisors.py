def findDivisors(num) :
    divider = 1
    while divider <= num :
        if (num % divider==0) :
            print(divider),
        divider = divider + 1
         
findDivisors(24)