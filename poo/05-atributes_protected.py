class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self._energy = 100

    def eat(self,food):
        print(f"{self.name} is eating {food.lower()}.") 

    def showinfo(self):
        print(f"{self.name} is {self.age} years old.")
        print("more Energy")

    def work(self):
        print(f"{self.name} is working.")   

    def _waste_energy(self,quantity):
        print("Less Energy")    
        self._energy -= quantity


person = Person("Marco",34)
person._energy=5 
person._waste_energy(6)

print(person._energy)