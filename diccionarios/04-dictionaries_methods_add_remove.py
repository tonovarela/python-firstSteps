user ={
    'name':"Varela",
    'age':80,
    'email':"tonovarela@live.com",
    'numbers':[1,2,3]
}

#copy
user2 = user.copy()
user2["name"]="Varelita"

# print(user2)

#pop
user.pop("name")
print(user)

#popitem Solo elimina el ultimo elemento

user.popitem()

print(user)

#update

user2.update({'name':"Tono","age":81})
print(user2)

#append

user["skills"]= user.get("skills",[])

user["skills"].append("Python")
user["skills"].append("Django") 
print(user)