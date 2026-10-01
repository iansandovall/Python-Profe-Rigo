cadena = "Esto es un ejemplo de cadena de texto"
print(cadena)
print(type(cadena)) #Preguntar por el tipo de dato de la varible

cadena1 = 'Ejemplo de "cadena" (con comillas simples)'
print(cadena1)

cadena_triple = """
Esto es un ejemplo de cadena con:
comillas triples.
Adios.
"""
print(cadena_triple)

#Escapar o saltar caracteres
cadena2 = "Esto es un \" ejemplo de cadena de texto"
print(cadena2)

#Salto de línea en cadenas
cadena_3 = "\n Esto es otro \n ejemplo de cadena"
print(cadena_3)

#Tabular una línea en cadenas
cadena_3 = "\t Esto es otro \t ejemplo de cadena"
print(cadena_3)

nombre = "Ian"
apellido = "Sandoval"
edad = 21

#Sumas 2 cadenas/concatenación
print(nombre + apellido)
print(nombre, apellido)

#Multiplicación de cadenas
print(nombre * 4)

print("Hola usuario: " + apellido)
print("Hola usuario: " , apellido)

print("El usuario: " + apellido, "tiene", edad, "años de edad")

numero = 30.5 #flotante
numero2 = "35" #string
#suma = numero + numero2 #No se pueden sumar 2 tipos de datos distintos

print( numero + int(numero2)) #Casting o casteo de datos (conversión entre tipos de datos)

numero3 = int(numero2)
print(type(numero3))
