#def find_divisors(num):
#    divisorlist = [x for x in range(1,num) if num%x == 0]
#    print(divisorlist)

def least_common_mult(num1,num2):
    lowestcommon = 1
    for potential in range(2,min(num1, num2)):
        if num1%potential == 0 and num2%potential == 0:
            lowestcommon = potential
            break
    return(lowestcommon)
