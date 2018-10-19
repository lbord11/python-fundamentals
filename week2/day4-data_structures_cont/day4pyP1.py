numbers = input("Numbers and Commas: ")
mybig = numbers.split(",")
x = []
y = []
for num in range(len(mybig)):
    mybig[num] =  int(mybig[num])
    if num%2 == 0:
        x.append(mybig[num])
    else:
        y.append(mybig[num])
print(x)
print(y)
final = list(zip(x, y))
print(final)
