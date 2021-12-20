class person:
    verb=10
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name, "\nAge:",self.age)
p1=person("Ananthu", 34)
p2=person("Manu", 23)
p1.display()
p2.display()
print("----------------------")
print("p1.name:",p1.name)
print("p1.age:",p1.age)
print("p2.name;",p2.name)
print("p2.age:",p2.age)
print("person.verb:",person.verb)
print("p1.verb:",p1.verb)
print("p2.verb:",p2.verb)
p1.verb=20
print("p1.verb:",p1.verb)
print("p1.verb:",p2.verb)
print("person.verb:",person.verb)
print("----------------------")
if(p1.age>p2.age):
    print(p1.name," is elder!")
else:
    print(p2.name," is elder!")

