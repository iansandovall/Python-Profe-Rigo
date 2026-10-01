#Sintáxis diccionario:: diccionario{clave:valor}
alumno = {"Nombre": "Rigo", "Contraseña": 12345, "Semestre": "sexto"}
print("Mi primer diccionario: ", alumno)
print("Tipo de estructura: ", type(alumno))
print("La longitud del diccionarios es. ", len(alumno))

#No se puede tener 2 claves con el mismo nombre, reemplaza su valor
#alumno = {"Nombre": "Rigo", "Contraseña": 12345, "Nombre": "Alfredo"}
#print(alumno)

#Acceder a los valores del diccionario
print("Nombre: ", alumno["Nombre"])
print(f"El alumno {alumno['Nombre']}, esta en {alumno['Semestre']} semestre")

#Acceder a las claves de un diccionario
print("Acceder a las claves de un diccionario")
print(alumno.keys())

#Acceder a los valores de un diccionario
print("Acceder a los valores de un diccionario")
print(alumno.values())

print("Acceder a los pares de datos de un diccionario")
print(alumno.items()) #Devuelve una lista con los pares de datos, clave, valor

#Agregar elementos a un diccionario
print("Agregando la clave Email: ")
alumno["Email"] = "iksg@iksg.com"
print(alumno)

alumno["Email"] = "iksg_10@iksg.com"
print(alumno)

Crear un diccionario llamado producto con:

nombre
precio
categoría

Después mostrar el producto y el precio.