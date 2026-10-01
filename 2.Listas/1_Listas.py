#Sintáxis de una lista
#mylist[]
lista = ["Python", 150, "Nombre", 3.1416, 6.29] #Una listase identifica por los corchetes
print(lista)
print("Tipo de estructura: ", type(lista))

print("Elemento de posición 3:", lista[3])
print("Longitud de la lista: ", len(lista))

ventas_diarias = [100, 125, 25, 697, 33, 74]
print("Ventas originales: ", ventas_diarias)

#Modificar valor de una lita, porque las listas son mutables
ventas_diarias[0] = 180
print("Actualización de ventas: ", ventas_diarias)

print("Dias hábiles: ", ventas_diarias[0:5])
print("Dias hábiles y ventas de fin de semana: ", ventas_diarias[-2:])

#Imprimir datos de una lista en posiciones impares
print(ventas_diarias[1: :2 ])

#Ciclo for
nums = [5, 15, 7, 20, 9, 15]
#Sintáxis del ciclo for, la i representa una variable
for i in nums:
    if nums[i] < 10:
        nums[1] = 0
    #print(i)
#print(numbs)