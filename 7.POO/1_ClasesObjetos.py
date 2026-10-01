#Sintaxis de una clase
# class <Nombre de la clase>():

class FabricaTelefonos():
    pass

print(type(FabricaTelefonos)) # <class 'type'>

celular = FabricaTelefonos() # Crear mi primer objeto, instanciación
print(type(celular))

celular2 = FabricaTelefonos() # Crear mi segundo objeto, instanciación
print(type(celular2))

def FabricaTelefonos(): #No debemos generar funciones o variables con el mismo nombre de la clase
    pass
print(type(FabricaTelefonos))