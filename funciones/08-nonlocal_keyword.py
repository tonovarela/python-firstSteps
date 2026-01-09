

def outer():
    enclosing_variable  ="Enclosing variable"
    def inner():
        nonlocal enclosing_variable
        enclosing_variable = "Enclosing modificado"
    inner()
    print(enclosing_variable)
        
        
        

outer()    