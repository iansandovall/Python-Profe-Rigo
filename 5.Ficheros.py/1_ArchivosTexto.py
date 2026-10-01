nombre = input("Ingresar tu nombre: ")
edad = input("Ingresar tu edad: ")
carrera = input("Ingresar tu carrera: ")

print(type(edad))

#Arbrir archivo en modo escritura 'w'
#Si el archivo no extste, lo crea con la ruta definido
archivo = open("perfil.txt", "w")

#Método write()
print("\nAquí uutilizamos el método write()")

#Escribir los datos en el archivo
archivo.write("Nombre: " + nombre + "\n")
archivo.write("Edad: " + edad + "\n")
archivo.write("Carrera: " + carrera + "\n")

archivo.close()

#Abrir elarchivo en modo lectura
print("\nAbrir el archivo en modo lectura")
archivo = open("perfil.txt", "r")

#Imprimir el contenido del documento
print("\nTexto del documento: ")
print(archivo.read())
archivo.close()