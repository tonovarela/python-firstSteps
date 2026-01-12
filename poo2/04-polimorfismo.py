class Animal:
    def smell(self):
        print("El animal esta oliendo")

    def make_sound(self):
        print("El animal esta haciendo sonido")

class Perro(Animal):
    def make_sound(self):
        print("El perro esta ladrando")


class Gato(Animal):
    def make_sound(self):
        print("El gato esta maullando")

class Jirafa(Animal):
    def do_something(self):
        pass
    


def make_noise(animal):
    if isinstance(animal,Animal):
        animal.make_sound()
    else:
        print("Esto no es un animal")    


perro = Perro()
gato = Gato()
jirafa = Jirafa()

make_noise(perro)
make_noise(gato)
make_noise(jirafa)