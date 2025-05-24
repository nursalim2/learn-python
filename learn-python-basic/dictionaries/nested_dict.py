myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linux",
        "year": 2011
    }
}

# accessing item
print(myfamily["child1"]["name"])

# looping item
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + " : ", obj[y])