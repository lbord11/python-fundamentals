status = "on"
vocab = set()
while status == "on":
    newword = input("Enter a word to add to the vocabulary: ")
    if newword == "q":
        status = "off"
    elif newword == "v":
        print(" ".join(vocab))
    else:
        vocab.add(newword)







#mystring = input("List of words with commas (some repeats): ")
#mylist = mystring.split(",")
#for num in range(len(mylist)):
#    mylist[num] = mylist[num].strip()
#myset = set(mylist)
#print(", ".join(myset))




#firststr = input("First set with commas: ")
#secondstr = input("Second set with commas: ")
#firstlist = firststr.split(",")
#firstset = set()
#for char in firstlist:
#    firstset.add(char.strip())
#secondlist = secondstr.split(",")
#secondset = set()
#for char in secondlist:
#    secondset.add(char.strip())
##print(firstset)
##print(secondset)
#overlap = firstset.intersection(secondset)
#print(", ".join(overlap))
