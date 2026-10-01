# EJERCICIO 2 | Información de alumnos

# Creamos el diccionario con los datos de los alumnos
alumnos = {
    "Ana": {"edad": 21, "calificacion": 85},
    "Pedro": {"edad": 22, "calificacion": 90},
    "Juan": {"edad": 20, "calificacion": 78},
    "María": {"edad": 21, "calificacion": 95}
}

suma_calificaciones = 0
aprobados = []
suma_edades = 0

# Recorremos el diccionario para mostrar nombre y calificación
for nombre in alumnos:
    calificacion = alumnos[nombre]["calificacion"]

    print("Nombre:", nombre, "- Calificación:", calificacion)

    # Sumamos las calificaciones para calcular el promedio
    suma_calificaciones = suma_calificaciones + calificacion

    # Revisamos qué alumnos aprobaron
    if calificacion >= 80:
        aprobados.append(nombre)
        suma_edades = suma_edades + alumnos[nombre]["edad"]

# Calculamos el promedio de calificaciones
promedio_calificaciones = suma_calificaciones / len(alumnos)

# Calculamos la edad promedio de los alumnos aprobados
promedio_edades = suma_edades / len(aprobados)

# Mostramos los resultados
print("Promedio de calificaciones:", promedio_calificaciones)
print("Alumnos aprobados:", aprobados)
print("Edad promedio de los alumnos aprobados:", promedio_edades)