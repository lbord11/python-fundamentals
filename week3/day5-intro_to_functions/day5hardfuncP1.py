def findfact(num):
    factorial = 1
    for x in range(1,num+1):
        factorial *= x
    return factorial


def findifprime(num):
    numstatus = "prime"
    for x in range(2,num):
        if num%x == 0:
            numstatus = "not prime"
            print("the lowest denominator is " + str(x))
            break
    print("The number you inputted is " + numstatus)
