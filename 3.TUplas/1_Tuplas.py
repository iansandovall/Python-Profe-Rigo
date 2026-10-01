#Sintáxis de una tupla
tupla = (1, 56.3, 85, "Python")
print(type(tupla))

#Aceeso por índices
print("Elemento de la posición 2: ", tupla[2])
print("indice del número 85: ", tupla.index(85))

numeros = (2, 5, 8, 9, 12, 45)

tupla3 = tupla + numeros
print("Concatenar tuplas: ", tupla3)

tupla[3] = "C++" ##Las tuplas no son mutables
print(tupla)