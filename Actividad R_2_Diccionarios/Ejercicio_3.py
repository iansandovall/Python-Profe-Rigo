# EJERCICIO 3 | Ventas de productos

# Creamos el diccionario con los productos y sus ventas
ventas = {
    "Laptop": 35,
    "Celular": 50,
    "Tablet": 28,
    "Audífonos": 75,
    "Smartwatch": 40,
    "Monitor": 60
}

# Buscamos el producto con mayor y menor cantidad de ventas
producto_mayor = max(ventas, key=ventas.get)
producto_menor = min(ventas, key=ventas.get)

# Calculamos el total y el promedio de ventas
total_ventas = sum(ventas.values())
promedio_ventas = total_ventas / len(ventas)

# Mostramos los resultados generales
print("Producto más vendido:", producto_mayor, "-", ventas[producto_mayor], "ventas")
print("Producto menos vendido:", producto_menor, "-", ventas[producto_menor], "ventas")
print("Total de ventas:", total_ventas)
print("Promedio de ventas:", promedio_ventas)

# Revisamos qué productos vendieron menos de 40 unidades
print("Productos que necesitan atención:")

for producto, cantidad in ventas.items():
    if cantidad < 40:
        print(producto, "-", cantidad, "ventas")

# Pedimos al usuario consultar las ventas de un producto
producto_buscar = input("Ingresa un producto: ")

# Buscamos el producto utilizando get()
resultado = ventas.get(producto_buscar, "Producto no encontrado")

# Mostramos el resultado de la búsqueda
print("Resultado:", resultado)