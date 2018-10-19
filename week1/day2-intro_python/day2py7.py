num1 = int(input("number:"))
num2 = int(input("number:"))
x = max(num1, num2)
lowestmultiple = num1*num2
while x < num1*num2:
    if x%num1 == 0 and x%num2 == 0:
        lowestmultiple = x
        break
    x += 1
print(lowestmultiple)
