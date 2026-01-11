class CoffeMaker:

    def make_coffe(self):
        self.__boil_water()
        self.__mix()
        print("PIP PIP")
        print("Tu cafe esta listo")

    def __boil_water(self):
        print("Hirviendo el agua")

    

    def __mix(self):
        print("Mezclando el agua")
 


coffe_maker =CoffeMaker()
coffe_maker.make_coffe()

