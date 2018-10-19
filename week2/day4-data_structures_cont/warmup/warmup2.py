my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', 'New York': 'New York City'}
neighbor_dct = {'New York': 'Albany', 'Ohio': 'Toledo'}
my_dct.update(neighbor_dct)
checkstate = input("New state: ").capitalize()
if my_dct.get(checkstate, "Get") == "Get":
    newcap = input("Captial of " + checkstate + ": ")
    my_dct.update({checkstate : newcap})
    print(my_dct)
else:
    print(my_dct.get(checkstate))
