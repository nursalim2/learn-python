thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# update
thisdict.update({"color" : ["red", "green", "blue"]})
print(thisdict)