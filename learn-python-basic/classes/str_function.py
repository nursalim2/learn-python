# without __str__()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person("Nursalim", 30)
print(p1)

# with __str__()
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"     
    
p2 = Person2("Nursalim", 30)
print(p2)
