#Lista de personas registradas al curso
nombres = ["Ana", "Pedro", "Juan", "María", "Luis", "Ana", "Andrea", "Juan", "Sofía", "Pedro", "Ariana"]
print("Lista original: ", nombres)

#Aquí se quitan los nombres repetidos
sin_repetidos = []
for i in nombres:
    if i not in sin_repetidos: #not in revisa que el nombre no este ya en la lista
        sin_repetidos.append(i)

sin_repetidos.sort() #Se ordena la lista alfabeticamente
print("Lista sin repetidos y ordenada: ", sin_repetidos)

#Se cuentan los nombres que comienzan con la letra A
con_a = []
for i in sin_repetidos:
    if i[0] == "A": #Con [0] se accede a la primera letra del nombre
        con_a.append(i)

print("Nombres que comienzan con A: ", con_a)
print(f"En total son: {len(con_a)} nombres")