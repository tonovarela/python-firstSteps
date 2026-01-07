

numbers = [1,2]

# Iterables.  Iterables, list, set, Tuplas, Diccionario 
# for number in numbers:
#     print(number)
    
iterator = iter(numbers)
# print(iterator)    
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

user ={
    'name':"Ricardo",
    'age':42,
    'can_swin':True
}

for key,value in user.items():      
    print(f"{key} -> {value}")
    