#def is_beer(num=0):
#    if num==0:
#        return("nope!")
#    elif num > 0:
#        return("yep! more!")

#def is_fan(name):
#    elsafans = {"Cary", "Josh", "Sean"}
#    return name in elsafans

def sumtogether(alist):
    sum = 0
    for num in alist:
        sum+= num
    return sum


def prod(alist):
    prod = 1
    for num in alist:
        prod*= num
    return prod

def findevens(alist):
    evens = []
    for num in alist:
        if num%2 == 0:
            evens.append(num)
    return evens


def findevens2(alist):
    evens = [num for num in alist if num % 2 == 0]
    return evens
