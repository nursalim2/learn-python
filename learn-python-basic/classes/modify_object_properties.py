class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Nursalim", 38)
p1.age = 30

print(p1.age)