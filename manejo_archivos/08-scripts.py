js_code ="""
console.log("Hola desde un archivos js generado en python");

const suma = (a,b)=> a+b
"""


with open("script_generado.js","w", encoding="utf-8") as archivo_js:
    archivo_js.write(js_code)
print("Archivo js generado correctamente")