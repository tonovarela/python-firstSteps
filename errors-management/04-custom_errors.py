
class InvalidAgeError(Exception):
      def __init__(self, age,message ="La edad debe ser mayor o igual a 18"):
          self.age = age
          self.message = message
          super().__init__(self.message)
          
          

def register_user(name,age):
    if age<18:
        raise InvalidAgeError(age)
    print(f"Usuario con nombre {name} y edad {age} ha sido registrado")  



try:
    register_user("Varela",10)
except InvalidAgeError as error:
    print(f"Error: {error}")                