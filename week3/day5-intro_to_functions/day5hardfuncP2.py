#1
def wordcount(string=""):
    wordcount = 1
    newstring = string.strip()
    if newstring == "":
        wordcount = 0
    else:
        for letter in newstring:
            if letter == " ":
                wordcount += 1
    return wordcount

#2
def wordcount2(string="",delimiter=" "):
    wordcount = 1
    newstring = string.strip()
    if newstring == "":
        wordcount = 0
    else:
        for letter in newstring:
            if letter == delimiter:
                wordcount += 1
    return wordcount

#3
def lettersperword(string="",delimiter=" "):
    lettercounts = []
    word = ""
    string = string.strip(delimiter)
    for letter in string:
        if letter == delimiter:
                lettercounts.append(len(word))
                word = ""
        else:
            word += letter
    if word != "":
        lettercounts.append(len(word))
    return lettercounts


#4
def allprimes(num):
    allprimes = []
    for item in range(2,num):
        status = "prime"
        for x in range(2,item):
            if item%x == 0:
                status = "not prime"
                break
        if status == "prime":
                allprimes.append(item)
    return allprimes

#5
def divisibility(list,divisor):
    yesno = []
    for number in list:
        if number % divisor == 0:
            yesno.append("yes")
        else:
            yesno.append("no")
    return yesno


#6
def lastletterwords(wordlist, letter):
    lastletterwords = []
    for word in wordlist:
        if word[len(word)-1].lower() == letter.lower():
            lastletterwords.append(word)
    return lastletterwords

#7
def find_substring_indexes(stringlist, shortstring):
    substringindexes = []
    x = 0
    while x < len(stringlist):
        if shortstring.lower() in stringlist[x].lower():
            substringindexes.append(x)
        x += 1
    return substringindexes

# Extra Credit
def taxes (listoftuples,income):
    listoftuples = sorted(listoftuples)
    newtuples = []
    sofar = 0
    for tuple in listoftuples:
        if income > tuple[0]:
            newtuples.append((tuple[0]-sofar,tuple[1]))
            sofar = tuple[0]
        else:
            newtuples.append((income-sofar,tuple[1]))
            break
    total = 0
    for tuple in newtuples:
        total += tuple[0]*tuple[1]
    print (newtuples)
    return (total)
