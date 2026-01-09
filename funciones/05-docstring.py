
def multiply(a:int,b:int)->int:
    return a*b


def hello(greet ,name="Invitado"):
    """
    Info: Esta es una funcion para devolver un saludo personalizado
    Args:
        greet (_type_): _description_
        name (str, optional): _description_. Defaults to "Invitado".
    """
    print(f"{greet} {name}")
    
    

hello(greet ="Hello",name="Varela")    


print(multiply(5,4))