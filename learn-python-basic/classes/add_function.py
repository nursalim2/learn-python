class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello my name is " + self.name)    

p1 = Person("Nursalim", 38)
p1.myFunc()