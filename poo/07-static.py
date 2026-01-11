class Person:
    species = "Homo sapiens" 
    
    @classmethod
    def change_species(cls,new_species):
        cls.species =new_species

    @staticmethod
    def metodo_statico():
        print("Metodo statico")
        
    def __init__(self,name,age):
        self.name  = name
        self.age = age

person1 = Person("Varela",21)

print(person1.species)
person1.change_species("Humanoide")
print(person1.species)


person2 = Person("varela",44)
print(person2.species)

Person.metodo_statico()