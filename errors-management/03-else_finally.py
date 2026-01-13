
def divide_numbers():
    try:
        a =int(input("Ingresa el numerador: "))
        b =int(input("Ingresa el denominador: "))    
        result = a /b
        print(result)    
        return result
    except ValueError:
        print("Por favor solo ingresa numeros")    
    except ZeroDivisionError:
        print("La division entre 0 no esta definida")
    except Exception as error:
        print(type(error))             
    finally:
        print("Me ejecuto")    
        
    
    
divide_numbers()    