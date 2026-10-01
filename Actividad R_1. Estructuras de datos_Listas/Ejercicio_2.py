# EJERCICIO 2

n = int(input("¿Cuántos elementos tendrá el vector? (máximo 10): ")) #input devuelve string, se convierte a int

#Si piden más de 10, se ajusta al máximo permitido que dice la instrucción
if n > 10:
    print("El máximo es 10, se tomarán solo 10 elementos")
    n = 10

vector = [] #Aquí se crea la lista vacia para el vector

#Después se llena el vector con los elementos, uno x uno
for i in range(n):
    numero = int(input("Ingresa un número entero: "))
    vector.append(numero)

print("Vector original: ", vector)

#Posteriormente se quitan los números repetidos
sin_repetidos = []
for i in vector:
    if i not in sin_repetidos: #not in revisa que el valor no este ya en la lista
        sin_repetidos.append(i)

sin_repetidos.sort() #Se ordena la lista de menor a mayor
print("Vector ordenado y sin repeticiones: ", sin_repetidos)