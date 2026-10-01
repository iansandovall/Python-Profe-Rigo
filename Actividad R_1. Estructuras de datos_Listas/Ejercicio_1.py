# EJERCICIO 1
 
n = int(input("¿Cuántas temperaturas vas a ingresar?: ")) #input devuelve string, se convierte a int
 
temperaturas = [] #Aquí se crear lista vacia
 
#Después se llena la lista con las temperaturas, una x una
#range(n) repite el ciclo n veces
for i in range(n):
    temp = int(input("Ingresa la temperatura: "))
    temperaturas.append(temp)
 
print("Temperaturas ingresadas: ", temperaturas)
 
#Aquí se calcula la media
total = sum(temperaturas) #Se suman elementos de una lista numerica
media = total / len(temperaturas)
print(f"La media de las temperaturas es: {media}")
 
#Se guardan las temperaturas mayores o iguales a la media
mayores = []
for i in temperaturas:
    if i >= media:
        mayores.append(i)
 
print(f"Temperaturas mayores o iguales a la media: {mayores}")
print(f"En total son: {len(mayores)} temperaturas")