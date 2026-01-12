

class Human:
    def __init__(self, name):
        self.name = name
        

    def speak(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


class Mutant(Human):
    def __init__(self, name,power):
        super().__init__(name)
        self.power = power

    def use_power(self):
        return f"{self.name} uses their power: {self.power}!"


class Person(Mutant):
    def __init__(self, name, age,occupation, power=None):
        super().__init__(name, power)
        self.age = age
        self.occupation = occupation
        

    def introduce(self):
        base_introduction = self.speak()
        return f"{base_introduction} I work as a {self.occupation}."


person = Person("Alice", 30, "Engineer", power="Invisibility")
print(person.speak())
print(person.introduce())       
print(person.use_power())  # This| will raise an AttributeError since Person doesn't inherit from Mutant properly 