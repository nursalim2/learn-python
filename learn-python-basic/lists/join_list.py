list1 = ["apple", "banana", "cherry"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# using append
for x in list2:
    list1.append(x)
print(list1)

# using extend
list1.extend(list2)
print(list1)