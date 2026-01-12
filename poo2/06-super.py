class Animal:
    def __init__(self, name):
        print("Inicializando Animal")
        self.name = name
    def _doir_som(self):
        print("Som do animal")    
    def fazer_som(self):
        raise NotImplementedError("Subclasses must implement this method")

class Cachorro(Animal):
    def __init__(self, name, raza):
        super().__init__(name)
        self.raza = raza

    def fazer_som(self):
        super()._doir_som()
        return "Au Au!"


perro = Cachorro("Rex", "Labrador")
print(perro.name)  
print(perro.raza) 
print(perro.fazer_som()) 
       