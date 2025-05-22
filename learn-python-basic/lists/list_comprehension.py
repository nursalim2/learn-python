# without comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# with comprehension
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)


# range
newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x%2 != 0]
print(newlist)

# expression
newlist = [x.upper() for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)



