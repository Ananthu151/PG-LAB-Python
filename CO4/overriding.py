class parent:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name:",self.name)

class child(parent):
    def __init__(self,name,add):
        parent.__init__(self,name)
        self.add=add
    def display(self):
        print("Name:",self.name)
        print("Address:",self.add)
c=child("Ananthu","Monthammyalil")
c.display()
