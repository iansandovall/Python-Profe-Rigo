meses_vendidos = ["Enero",  "Febrero",  "Marzo", "Abril",  "Mayo"]
ventas = [1200, 1450, 980, 1780, 1350]

# Reto: Separar meses y números
total_ventas = sum(ventas) #Sumas elementos de una lista númerica
promedio_Ventas = total_ventas/len(ventas)
print(f"El promedio de ventas es: ${promedio_Ventas}")

mejor_mes_indice = ventas.index(max(ventas))
mejor_mes = meses_vendidos[mejor_mes_indice]

print(f"Mejor mes: {mejor_mes} con ${max(ventas)}")


##Llenar una lista
#Crear lista vacia
listav = [] #Crear lista vacía
print(type(listav))
#Método para llenar una lista
edad = int(input("Ingresa tu edad: ")) #input devuelve string
#Convertir string a int
print(type(edad))
listav.append(edad)
print(f"La edad del usuario es: {listav}")
print(f"La edad del usuario es: {listav[0]}")