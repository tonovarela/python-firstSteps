try:
    with open("permisos.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("No tienes permiso para abrir este archivo")    
except Exception as error:
    print(f"Ocurrio un error {error}")
    