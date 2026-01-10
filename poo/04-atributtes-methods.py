class Person:
    specie ="Humans"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self,food):
        print(f"{self.name} is eating {food.lower()}.") 

    def showinfo(self):
        print(f"{self.name} is {self.age} years old.")
        print(f"{self.name} belongs to the specie {self.specie}.")
        print("more Energy")

    def work(self):
        print(f"{self.name} is working.")   

       




person1 = Person("Marco",43)

person1.showinfo()
person1.work()
person1.eat("Pizza")

