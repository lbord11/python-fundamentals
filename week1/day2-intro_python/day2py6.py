num1 = int(input("number:"))
num2 = int(input("number:"))
x = min(num1, num2)
lowestcommon=1
while x > 0:
    if num1%x == 0 and num2%x == 0:
        lowestcommon = x
        break
    x -= 1
print(lowestcommon)
