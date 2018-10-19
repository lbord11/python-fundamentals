#print("#1 Only even numbers")
#end = int(input("end num: "))
#alllist = list(range(0,end+1))
#newlist = alllist[0::2]
#print(newlist)

#print("#2 Only divisible numbers")
#largenum = int(input("Large number to check until: "))
#divnum = int(input("Num to divide by: "))
#numset = list(range(largenum+1))
#divset = []
#for num in numset:
#    if num%divnum == 0:
#        divset.append(num)
#print(divset)


#print("#3: Fina common values in lists")
#lista = [0, 3, 6, 9, 10, 2, 5]
#listb = [2, 6, 4, 7, 8, 1, 15]
#common = []
#for numa in lista:
#    for numb in listb:
#        if numa == numb:
#            common.append(numa)
#common.sort()
#print(common)



#print("#4 Only divisible numbers")
#largenum = int(input("Large number to check until: "))
#divnum = int(input("Num to divide by: "))
#numset = list(range(largenum))
#divset = []
#for num in numset:
#    if num%divnum == 0:
#        divset.append(num)
#print(divset)



print("Extra: build 2 lists; find same values")
lista = []
for x in range(0,7):
    addon = int(input("new num in A: "))
    lista.append(addon)
print(lista)
listb = []
for x in range(0,7):
    addon = int(input("new num in B: "))
    listb.append(addon)
print(listb)
common = []
for numa in lista:
    for numb in listb:
        if numa == numb:
            if numa in common:
                continue
            else:
                common.append(numa)
common.sort()
print(common)
