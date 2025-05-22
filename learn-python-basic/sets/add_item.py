# using add method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

print(thisset)

# add another set to current set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# add any iterable
thisset = {"apple", "banana", "cherry"}
thislist = ["pineapple", "mango", "papaya"]
thisset.update(thislist)
print(thisset)