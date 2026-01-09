
global_variable = "Soy global"



def outer_function():
    print("Imprimiendo desde la funcion ")
    local ="Soy local"
    print(local)
    print(global_variable)
    


print(global_variable)
outer_function()
# local solo se ve desde outer_function
#print(local)
