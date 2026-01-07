# Conjuntos


my_set = {1, 2, 3, 4, 5}

my_set.add(6)
my_set.add(6)
my_set.add(8)
print(my_set)

#remove 

my_set.remove(3)
print(my_set)

#No marca error si no existe
my_set.discard(3)
print(my_set)

my_set.discard(1)
print(my_set)

#Elimina un elemento al principio y lo devuelve

print(my_set.pop())
print(my_set.pop())
print(my_set)