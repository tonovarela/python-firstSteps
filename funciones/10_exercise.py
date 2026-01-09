import random
import string

caracteres = string.ascii_letters + string.digits+ string.punctuation
def password_generator(longitud):        
    password_generado =[]    
    for _ in range(longitud):
        letter =random.choice(caracteres)
        password_generado.append(letter)                
    return ''.join(password_generado)     

longitud = int(input("Cuantos caracteres quieres en tu contraseña: "))
password = password_generator(longitud)
print(f"La contraseña es {password}")