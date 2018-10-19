
#.1
#thestring = input("String: ").lower()
#theletter = input("One letter: ").lower()
#totaloccurances = 0
#for char in thestring:
#    if char == theletter:
#        totaloccurances += 1
#print(totaloccurances)


#.2
#thestring = input("A string: ").lower()
#if thestring[len(thestring)-1] == "!":
#    thestring = thestring.upper()
#print(thestring)


#print("#3 Remove Vowels")
#thestring = input("a string: ")
#vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
#newstring = ""
#for letter in thestring:
#    if letter not in vowels:
#        newstring += letter
#print(newstring)



print("#3 Make every other letter capitalized")
thestring = input("string: ")
stringnospaces = ""
for letter in thestring:
    if letter != " ":
        stringnospaces += letter
capstring = ""
for num in range(len(stringnospaces)):
    if num%2 == 0:
        capstring += stringnospaces[num].upper()
    else:
        capstring += stringnospaces[num].lower()
cs = 0
ts = 0
finalstring = ""
while ts < len(thestring):
    if thestring[ts].lower() == capstring[cs].lower():
        finalstring += capstring[cs]
        cs += 1
        ts += 1
    else:
        finalstring += " "
        ts += 1
print(finalstring)






#print("LIST #3")
#lista = [0, 3, 6, 9, 10, 2, 5]
#listb = [2, 6, 4, 7, 8, 1, 15]
#common = []
#for numa in lista:
#    for numb in listb:
#        if numa == numb:
#            common.append(numa)
#common.sort()
#print(common)
