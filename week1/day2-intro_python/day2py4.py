findfact = int(input("fact number:"))
factorial = 1
x = findfact
while x > 0:
    factorial *= x
    x -= 1
print(factorial)
