'''
Crear un carrito de compras que haga las siguientes funciones
Agregar producto
Eliminar producto
Mostrar la lista ordenada
Buscar producto
Contar productos del carrito
Vaciar el carrito
'''

print("----- Carrito de compras -------")
option=0
shopping_cart = ["Laptop","Vaso","Cafe","Audifonos"]
while(option!= "7" ):
    
    print("----Opciones------")
    print("1.- Agregar producto")
    print("2.- Eliminar producto")
    print("3.- Mostrar la lista ordenada")
    print("4.- Buscar producto")
    print("5.- Contar productos del carrito")
    print("6.- Vaciar el carrito")
    print("7.- Salir")
        
    option = input("Elige una opcion (1-7): ")
    print()
    if option == "1":
        name_product = input('Capture el nombre del nuevo producto: ')
        shopping_cart.append(name_product)
        
    elif option == "2":
        name_product = input('Capture el nombre del  producto a eliminar: ')
        if name_product not in shopping_cart:
            print("El producto no existe")
        else:
            shopping_cart.remove(name_product)
            print("Producto eliminado correctamente")
            

    elif option == "3":
        print(sorted(shopping_cart))    
    elif option == "4":
        name_product = input('Capture el nombre del  producto a buscar: ')
        if (name_product not in shopping_cart):
            print("El producto no existe")
        else:
            print("Se encontro el producto")

    elif option == "5":
        print(f"Total de productos: {len(shopping_cart)}")
    elif option == "6":
        shopping_cart.clear()
        print("Se ha vaciado el carrito del producto")
    elif option == "7":    
        print(" Adios ")
    else:
        print("Opcion no valida")
        
    print()
    
    

