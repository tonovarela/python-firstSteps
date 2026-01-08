nested_dict = {
    "Persona1":{"nombre":"Marco","edad":29},
    "Persona2":{"nombre":"Maria","edad":56},
    "Persona3":{"nombre":"Alberto","edad":40},
}

for key,value in nested_dict.items():
    print(f"{key}")
    for sub_key,sub_value in value.items():
        print(f"{sub_key} - {sub_value}")



