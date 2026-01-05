# 🐍 Primeros Pasos con Python

Repositorio con ejercicios básicos para aprender los fundamentos de Python.

## 📚 Contenido

### Primitivas

#### 01 - Hola Mundo
**Archivos:**  
- `primitivas/01-hola_mundo.py`  
- `primitivas/01-hello_world.py`

Primer programa en Python mostrando un mensaje en consola.

```bash
python3 primitivas/01-hola_mundo.py
python3 primitivas/01-hello_world.py
```

#### 02 - Comentarios
**Archivo:** `primitivas/02-comments.py`

Uso de comentarios de una y varias líneas en Python.

```bash
python3 primitivas/02-comments.py
```

#### 03 - Variables
**Archivo:** `primitivas/03-variables.py`

Declaración y uso de variables:
- Strings
- Números enteros
- Floats
- Convenciones de nombres

```bash
python3 primitivas/03-variables.py
```

#### 04 - Tipos de Datos
**Archivo:** `primitivas/04-data_types.py`

Tipos de datos básicos:
- `str`
- `int`
- `tuple`
- `set`
- `dict`

```bash
python3 primitivas/04-data_types.py
```

#### 05 - Strings
**Archivo:** `primitivas/05-string.py`

Trabajo con cadenas:
- Strings de una y varias líneas
- Concatenación
- F-strings para formateo

```bash
python3 primitivas/05-string.py
```

#### 07 - Índices de Strings
**Archivo:** `primitivas/07-string-indexes.py`

Manipulación de cadenas usando índices:
- Acceso a caracteres individuales
- Slicing (cortar cadenas)
- Invertir cadenas con `[::-1]`

```bash
python3 primitivas/07-string-indexes.py
```

#### 08 - Inmutabilidad
**Archivo:** `primitivas/08-inmutable.py`

Demostración de que los strings en Python son inmutables.

```bash
python3 primitivas/08-inmutable.py
```

#### 09 - Conversiones de Tipo
**Archivo:** `primitivas/09-conversions.py`

Conversión entre diferentes tipos de datos:
- `int()` - Convertir a entero
- `str()` - Convertir a string
- `float()` - Convertir a decimal

```bash
python3 primitivas/09-conversions.py
```

#### 10 - Operaciones Matemáticas
**Archivo:** `primitivas/10-math_operations.py`

Operaciones matemáticas básicas:
- Suma, resta, multiplicación, división
- Potencia (`**`)
- División entera (`//`)
- Módulo (`%`)
- Funciones: `round()`, `abs()`

```bash
python3 primitivas/10-math_operations.py
```

#### 11 - Funciones Incorporadas
**Archivo:** `primitivas/11-incorporated_functions.py`

Funciones y métodos nativos de Python:
- `type()` - Obtener el tipo de dato
- `.upper()` - Convertir a mayúsculas
- `.replace()` - Reemplazar texto

```bash
python3 primitivas/11-incorporated_functions.py
```

#### 12 - Input
**Archivo:** `primitivas/12-input.py`

Captura de datos del usuario con la función `input()`.

```bash
python3 primitivas/12-input.py
```

#### 13 - Proyecto Final (Primitivas)
**Archivo:** `primitivas/13-last.py`

Proyecto que combina todos los conceptos aprendidos:
- Captura de datos con `input()`
- Uso de diccionarios
- F-strings para formateo
- Operaciones matemáticas simples
- Manipulación básica de strings

```bash
python3 primitivas/13-last.py
```

---

### Condicionales

#### 01 - If Condicional
**Archivo:** `condicionales/01-if_condicional.py`

Introducción a las estructuras condicionales:
- Declaración `if`
- Cláusula `else`
- Evaluación de booleanos

```bash
python3 condicionales/01-if_condicional.py
```

#### 02 - Elif Condicional
**Archivo:** `condicionales/02-elif_conditional.py`

Condiciones múltiples con `elif`:
- Múltiples condiciones
- Flujo de control con `elif`
- Uso de `pass` para bloques vacíos

```bash
python3 condicionales/02-elif_conditional.py
```

#### 03 - Operador Ternario
**Archivo:** `condicionales/03-ternary_operator.py`

Uso del operador ternario para simplificar condicionales en una sola línea.

```bash
python3 condicionales/03-ternary_operator.py
```

#### 04 - Truthy y Falsey
**Archivo:** `condicionales/04-truthy-falsey.py`

Valores que se consideran verdaderos (`truthy`) o falsos (`falsey`) en Python.

```bash
python3 condicionales/04-truthy-falsey.py
```

#### 05 - None
**Archivo:** `condicionales/05-none.py`

Uso de `None` como valor nulo y su evaluación en condicionales.

```bash
python3 condicionales/05-none.py
```

#### 06 - Operadores Lógicos
**Archivo:** `condicionales/06-logical_operators.py`

Operadores lógicos:
- `and`
- `or`
- `not`

```bash
python3 condicionales/06-logical_operators.py
```

#### 07 - Operadores de Comparación
**Archivo:** `condicionales/07-comparation_operatos.py`

Operadores de comparación:
- `==`, `!=`
- `>`, `<`
- `>=`, `<=`

```bash
python3 condicionales/07-comparation_operatos.py
```

#### 08 - Operadores de Pertenencia
**Archivo:** `condicionales/08-membership_operators.py`

Operadores de pertenencia:
- `in`
- `not in`

Aplicados a rangos, listas y strings.

```bash
python3 condicionales/08-membership_operators.py
```

#### 09 - Igualdad vs Identidad
**Archivo:** `condicionales/09-is_equal.py`

Diferencia entre:
- `==` (igualdad de valor)
- `is` (identidad en memoria)

```bash
python3 condicionales/09-is_equal.py
```

#### 10 - Short Circuiting
**Archivo:** `condicionales/10-short_circuiting.py`

Corto circuito en expresiones lógicas con `and` y `or`.

```bash
python3 condicionales/10-short_circuiting.py
```

#### 11 - Flujo de Control por Edad
**Archivo:** `condicionales/11-control_flow.py`

Ejemplo completo de flujo de control:
- Clasificación de una persona según su edad usando `if / elif / else`.

```bash
python3 condicionales/11-control_flow.py
```

#### 12 - Proyecto Final (Condicionales)
**Archivo:** `condicionales/12-proyecto_final.py`

Evaluador de candidatos para Recursos Humanos:
- Uso de diccionarios
- Validación de habilidades (`Python` y `Django`)
- Clasificación por años de experiencia
- Uso de `.upper()`, `in` y `split()`

```bash
python3 condicionales/12-proyecto_final.py
```

---

## 🚀 Ejecutar los Archivos

Asegúrate de tener Python 3 instalado:

```bash
python3 --version
```

Para ejecutar cualquier archivo:

```bash
python3 ruta/del/archivo.py
```

Ejemplos:

```bash
python3 primitivas/01-hola_mundo.py
python3 condicionales/01-if_condicional.py
```

## 📝 Conceptos Aprendidos

- ✅ Sintaxis básica de Python  
- ✅ Variables y tipos de datos  
- ✅ Strings y manipulación de texto  
- ✅ Colecciones: tuplas, sets y diccionarios  
- ✅ Operaciones matemáticas  
- ✅ Funciones incorporadas  
- ✅ Input del usuario  
- ✅ F-strings  
- ✅ Condicionales (`if`, `elif`, `else`)  
- ✅ Booleanos y evaluación de condiciones  
- ✅ Operadores lógicos y de comparación  
- ✅ Operadores de pertenencia (`in`, `not in`)  
- ✅ Igualdad vs identidad (`==` vs `is`)  

## 🛠️ Requisitos

- Python 3.x

## 📖 Recursos Adicionales

- [Documentación oficial de Python](https://docs.python.org/es/3/)
- [Tutorial de Python en español](https://docs.python.org/es/3/tutorial/)

---

💡 **Tip:** Experimenta modificando los archivos para practicar y entender mejor cada concepto.