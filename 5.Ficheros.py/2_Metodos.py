# Entraremos de nuevo al archivo para observar algunos métodos que podemos aplicar
archivo = open("perfil.txt", "r")

print("Tipo:", type(archivo))
print("Modo:", archivo.mode)
print("Codificación:", archivo.encoding)

archivo.close()

# read(): permite indicar la cantidad de bytes del mensaje que queremos mostrar.
#  Si lo indicamos vacio o con -1, se mostrará todo el texto

archivo = open("perfil.txt", "r")
print("\nMétodo read()")
contenido = archivo.read(7) #Si se le pasa un argumento, signific el número de bytes a imprimir
print(contenido)
# Cerraremos el archivo
archivo.close()


archivo = open("perfil.txt", "r")

# readline(): retorna una linea del archivo
print("\nMétodo readline():")
print(archivo.readline())
#print(archivo.readline())

# readable(): retorna True si el texto es legible, es decir, se deja leer; por el contrario, retornará False
print("\nMétodo readable():")
print(archivo.readable())

archivo.close()

archivo = open("perfil.txt", "r")
# readlines(): retorna una lista que contiene cada línea del archivo como un elemento de la misma
print("\nMétodo readlines():")
print(archivo.readlines())

archivo.close()

if archivo.closed: 
    print("El archivo se ha cerrado correctamente" )
else: 
    print("El archivo permanece abierto")
