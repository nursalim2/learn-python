import json

# json string
x = '{"name":"John", "age":30, "city":"New york"}'

# parsing json
y = json.loads(x)

print(y)
print(y["age"])
