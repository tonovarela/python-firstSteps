
''' Intrucciones:
Crearas un programa de evaluacion  de candidatos potenciales con conocimientos en Python para RH.
Obtendras el nombre, años de experiencia y habilidades

Evaluaras
* Si el candidato sabe Python/Django tiene +3 de experiencia: Candidato Optimo
* Si el candidato sabe Python/Django tiene +1 de experiencia: Buen Candidato
* Si el candidato sabe Python/Django : Posible candidato
* Si el candidato no sabe Python: No optimo, se guarda su CV
Ocupar el metodo split
'''

registro ={
    "nombre":"Marco",
        # input(" Captura tu nombre:"),
    "habilidades": "Python/D",
        # input("Captura tus habilidades: "),
    "experiencia":"0"
        # input("Captura tu años de experiencia: ")
}
tiene_habilidades_requeridas ="PYTHON"  in registro["habilidades"].upper()  and "DJANGO" in registro["habilidades"].upper() 
anios_experiencia = int(registro["experiencia"])

print(registro["habilidades"].split("/"))

if tiene_habilidades_requeridas and  anios_experiencia>=3 :
    print("Candidato optimo") 
elif tiene_habilidades_requeridas and anios_experiencia>=1:
    print("Buen candidato")     
elif tiene_habilidades_requeridas:
    print("Posible candidato")    
else:
    print("Se guarda su curriculum")    
