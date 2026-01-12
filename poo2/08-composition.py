
class Flyer:
    def fly(self):
        print("Puedo volar")
        
    def do_something(self):
        print("FlyFly")        

class Swimmer:
    def swim(self):
        print("Puedo nadar")
        
    def do_something(self):
        print("Swim-Swin")        
                
            
class Duck:
    def __init__(self):
        self.flyer  =Flyer()
        self.swimmer = Swimmer()
        
    def quack(self):
        print("Quack ....")
        
    def start_fly(self):
        self.flyer.fly()
    
    def start_swim(self):
        self.swimmer.swim();        
            
    
    
    
donald= Duck()
donald.start_fly()
donald.start_swim()
