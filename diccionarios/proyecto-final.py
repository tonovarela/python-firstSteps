students  ={
    "Ana":{"calificaciones":[8,7,9]},
    "Luis":{"calificaciones":[6,5,7]},
    "Sofia":{"calificaciones":[10,9,10]}
}

#Agregar nuevo estudiante
#Saca el promedio de un estudiante existente
# El promedio del estudiante nuevo

students["Marco"]={"calificaciones":[10,10,10]}

for name_student in students:
    student = students[name_student]
    promedio = sum(student["calificaciones"])/len(student["calificaciones"])
    student["promedio"]=promedio
    print(f"El alumno {name_student} tiene un promedio de {student['promedio']:.2f} con las calificaciones {student['calificaciones']}   ")

promedio_general = sum( students[name_student]['promedio'] for name_student in students) / len(students)

print(f"El promedio de todos los estudiantes es {promedio_general:.2f}")