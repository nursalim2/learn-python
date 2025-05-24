# loop key
thisdict = {
    "brand": "Ford",
    "name": "Mustang",
    "year": 1976
}

for x in thisdict:
    print(x)

for x in thisdict.keys():
    print(x)


# loop values
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x) 

# loop item (key, value)       
for x, y in thisdict.items():
    print(x, y)