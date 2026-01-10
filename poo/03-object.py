class Person:
    def __init__(self,name,age):
        if (age > 18):
            self.name = name
            self.age = age

        
      
    



person1 = Person("Marco",43)
print(person1)
print(f"Nombre: {person1.name}  y edad {person1.age}")

person2  = Person("Varela",43)
print(person2)
print(f"Nombre: {person2.name}  y edad {person2.age}")