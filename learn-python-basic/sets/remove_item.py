# using remove() method
# will cause error if item is not exists
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

print(thisset)

# using discard
thisset.discard("mango")
print(thisset)

# using pop
thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)

# using clear
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# del
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)