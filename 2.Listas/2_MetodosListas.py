# CONTEXTO: Análisis de calificaciones de productos
calificaciones = [4, 5, 3, 4, 2, 5, 4, 3, 4, 1, 5]
print("Calificaciones:", calificaciones)

#Agregar elementos a la lista en la última posición
calificaciones.append(3)
print("Calificaciones actualizadas:")

#Método insert, para colocar un nuevo elemento en una posición particular
#lista.insert(posición, elemento) # posición es el índice donde se quiere insertar el elemento

calificaciones.insert(2, 5)
print("Calificaciones con método insert: ", calificaciones)

calificaciones.insert(-2, 10)
print("Calificaciones con método insert: ", calificaciones)


# MÉTODO COUNT -  cuenta cuántas veces se repite el parámetro
productos_5_estrellas = calificaciones.count(5)
#Sintáxis para format
print(f"Productos con 5 estrellas:{productos_5_estrellas} productos)")
posición_primera_mala = calificaciones.index(1)
print(f"Primera calificación baja en la posición:{posición_primera_mala}")


# Método index - devuelve la posición del primer elemento que encuentre, solo del primer
print(f"Primera calificación baja en la posición:(posición_primera_mala)")


# MÉTODO SORT - Análisis ordenado
calificaciones_copia = calificaciones.copy()  # Buena práctica
calificaciones_copia.sort() #Ordenar lista de manera ascendente



#Métodos para eliminar elementos en las listas
# El primero será pop

print("Método pop")
calificaciones.pop(0) #Si tiene argumentos, elimina el valor de la 

#print("Método pop")
#calificaciones.pop(1) #Si tiene argumetos, elimina el valor en esa posición


#Eliminar con remove

#print(calificaciones)
#Elimina por valor, no por posición
calificaciones.remove(1)



# Métodos in / not in
titulo = ['t','u','t','o','r','i','a','l']
# in operator
#if 't' in titulo:
   ##Count - método de las listas que sirve para contar cuántas veces se repite un elemento en la lista
   
   #n = titulo.count('t')
   #print(f"La letra t se repite {n} veces")
   
