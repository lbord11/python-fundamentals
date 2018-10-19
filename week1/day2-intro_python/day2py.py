x = int(input('number: '))
if x > 0:
    print("Positive")
elif x < 0:
    print("negative")
else:
    print(0)

print(" ------ ")

first = int(input("first number:"))
second = int(input("second num:"))
if first > second:
    print("first greater")
elif first == second:
    print("equal")
else:
    print("second is greater")

print ("-----------")

end = int(input("end number:"))
total = 0
x = end
while x > 0:
    total += x
    x -= 1
print(total)
