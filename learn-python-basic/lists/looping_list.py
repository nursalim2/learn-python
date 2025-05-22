thislist = ["apple", "banana", "cherry"]

for x in thislist:
    print(x)

# looping using index
print("\n=============")

for i in range(len(thislist)):
    print(thislist[i])

print("\n=============")

# using while
i = 0

while i < len(thislist):
    print(thislist[i])
    i = i + 1

print("\n=============")

# using list comprehension
[print(x) for x in thislist]