thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

# using get
x = thisdict.get("model")
print(x)

# items()
# return each item in a dictionary
x = thisdict.items()
print(x)