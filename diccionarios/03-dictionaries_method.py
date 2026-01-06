user ={
    'name':"Varela",
    'age':80,
    'email':"tonovarela@live.com",
    'numbers':[1,2,3]
}

# print(user.get('name'))
#Solo en keys
print("name" in user)
print(user.values())
print(user.keys())

print(80 in user.values())