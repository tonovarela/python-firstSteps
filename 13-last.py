# Recibir de manera dinamica, nombre ,año de nacimiento, correo y password

print("Por favor ingresa los siguientes datos:")

registro ={
    "nombre" :input("Cual es tu nombre? "),
    "año de nacimiento":input("Cual es tu año de nacimiento? "),
    "correo" :input("Cual es tu correo? "),
    "password" :input("Cual es tu password? ")
}


info = f"""
Nombre: {registro['nombre']}
Año de nacimiento: {registro['año de nacimiento']}
Correo: {registro['correo']}
Tendras {2050 - int(registro['año de nacimiento'])} años en el 2050
Password: {'*' * len(registro['password'])}
"""

print(info)