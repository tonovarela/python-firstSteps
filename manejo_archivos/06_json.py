import json

users = { "nombre":"Varela","edad":43,"active":True}

with open("datos.json","w") as file:
    json.dump(users,file,indent=4)


with open("datos.json","r") as file:
    data=json.load(file)
    print(data)
