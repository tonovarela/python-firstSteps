

from abc  import ABC, abstractmethod
# Clase abstracta

class Animal(ABC):        
    @abstractmethod 
    def sound(self):
        pass
    def do_something(self):
        print("Here")
        
        
    
class Dog(Animal):    
     def sound(self):
        print("Guau ")

class Cat(Animal):
    def sound(self):
        print("Miau ")



taquito = Dog()
taquito.sound()
taquito.do_something()

print("------------------")

gatito = Cat()
gatito.sound()
gatito.do_something()