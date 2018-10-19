#numbers = input("Numbers and Dashes: ")
#splitit = numbers.split("-")
#print(splitit)
#mydict = {}
#for item in splitit:
#    num = int(item)
#    square = num*num
#    mydict.update({num:square})
#print(mydict)


#state_dictionary = {'New York': 'Albany', 'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento','Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln', 'Oregon': 'Salem', 'Texas': 'Austin'}
#statecase = {}
#for key, value in state_dictionary.items():
#    key = key.title()
#    value = value.title()
#    statecase.update({key:value})
#getstate = input("State Name: ").title()
#print(statecase.get(getstate, "Capital Unknown"))

coords = {}
enteringnewcoords = 1
while enteringnewcoords == 1:
    newcoord = input("Please enter a coordinate-word pair in the format (x, y, word): ")
    if newcoord == "":
        enteringnewcoords = 0
    else:
        workinglist = newcoord.split(",")
        workingtuple = (int(workinglist[0]), int(workinglist[1]))
        workingword = workinglist[2].strip()
        coords.update({workingtuple: workingword})
keyhints = set()
for coord in coords:
    keyhints.add(coord)
print("Key Hints: " + str(keyhints))
enterexistingcoords = 1
while enterexistingcoords == 1:
    retrievestr = input("Please enter a coordinate to look up: ")
    if retrievestr == "q":
        enterexistingcoords = 0
    else:
        retrievelist = retrievestr.split(",")
        retrievetup = (int(retrievelist[0]), int(retrievelist[1]))
        print(coords.get(retrievetup, "Coord not found"))
print("DONE!")
