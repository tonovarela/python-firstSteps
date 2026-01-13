class InvalidAgeError(Exception):
      def __init__(self, age,message ="La edad debe ser mayor o igual a 18"):
          self.age = age
          self.message = message
          super().__init__(self.message)
          
class InvalidEmailException(Exception):
        def __init__(self,message ="Esto no parece ser un correo electronico"):
         self.message =message
         super().__init__(self.message)
        

def register_user(name,age,email):
    if age < 17:
        raise InvalidAgeError(age)
    if "@" not in email or "." not in email.split("@")[-1]:
        raise InvalidEmailException()
    
    print(f"Usuario con nombre {name},edad {age} y correo electronico {email} ha sido registrado")  
    

try:
    register_user("Varela",40,"tonovarela@live.com")
except InvalidAgeError as error:
    print(f"Error: {error}")    
except InvalidEmailException as error:
    print(f"Error: {error}")    
except Exception as error:
    print(f"Error: {error}")    
      
        
          
    
    



