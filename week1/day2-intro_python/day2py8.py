num1 = int(input("number:"))
x = num1 - 1
default = "prime"
while x > 1:
    if num1%x == 0:
        default = "not prime"
        break
    x -= 1
print(default)
