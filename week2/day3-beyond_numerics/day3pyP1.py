#findfact = int(input("fact number:"))
#factorial = 1
#for x in list(range(1,findfact+1)):
#    factorial *= x
#print(factorial)

findpm = int(input("fact number:"))
default = "prime"
for x in list(range(2,findpm)):
    if findpm%x == 0:
        default = "not prime"
        print("the lowest denominator is " + str(x))
        break
print(default)
