
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
                
            
class Duck(Swimmer,Flyer):
    def quack(self):
        print("Quack ....")
    
        
        

donald= Duck()
donald.fly()
donald.quack()      
donald.do_something()
                
print(Duck.__mro__)