

try:
    my_file= open("text.txt")
    # print(my_file.read())
    # my_file.seek(0)    
    # print(my_file.read())
    print(my_file.readline())
    print(my_file.readlines())
    
    my_file.close()
except FileNotFoundError as error:
    print("El archivo no existe")
except Exception as _:
    print("Hubo un error")    
    

    


