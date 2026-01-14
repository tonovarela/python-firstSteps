
import csv

with open("datos.csv", "w",newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Nombre","Edad"])
    writer.writerow(["Antonio",43])
    writer.writerow(["Varela",41])
    writer.writerow(["Ximena",2])


with open("datos.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


