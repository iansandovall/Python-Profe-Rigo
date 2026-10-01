# EJERCICIO 1 | Capitales de países

# Creamos el diccionario con los países y sus capitales
capitales = {
    "Guatemala": "Ciudad de Guatemala",
    "El Salvador": "San Salvador",
    "Honduras": "Tegucilapa",
    "Nicaragua": "Managua",
    "Costa Rica": "San Jose",
    "Panama": "Panama",
    "Argentina": "Buenos Aires",
    "Colombia": "Bogota",
    "Venezuela": "Caracas",
    "España": "Madrid"
}

# Pedimos al usuario que ingrese un país
pais = input("Ingresa el nombre de un país: ")

# Buscamos el país con el método get()
capital = capitales.get(pais, "El país ingresado no se encuentra")

# Mostramos el resultado
print("Resultado:", capital)