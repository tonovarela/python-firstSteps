# dunder

class Person:

    
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"Hola mi nombre es {self.name} "    
    def __len__(self):
        return len(self.name)



persona = Person("Varela")        
print(persona)
print(len(persona))