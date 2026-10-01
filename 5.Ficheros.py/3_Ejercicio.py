ruta = "ventas_2026.txt"

  #Método with/as cierra automáticamente el archivo, 
   
with open(ruta, mode="r", encoding="utf-8") as fichero:
  
    datos = fichero.readlines()

    print(datos)

    #Inicializar variables
    #¿Cómo podemos separar "Laptop" y "15000"?
    print(datos[0])

    total = 0 #Declaración de variable afuera del for (porque se estará llenando en el for)

    for linea in datos:
        #Strip elimina espacios y saltos de línea, y split separa mediante
        partes = linea.strip().split(",")
        print(partes)

        producto = partes[0]
        precio = int(partes[1])

        total = total + precio

    print("Total de ventas: ", total)



   
if fichero.closed: 
    print("El archivo se ha cerrado correctamente" )
else: 
    print("El archivo permanece abierto")
