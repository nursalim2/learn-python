thistuple = ("apple", "banana", "cherry")
thislist = list(thistuple)
thislist[1] = "kiwi"
thistuple = tuple(thislist)

print(thistuple)