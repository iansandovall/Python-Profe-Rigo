class FabricaTelefonos():
    marca = "Apple" #Atributo

    def ElaborarHuawei(self): #Metodo de instancia, porque tiene la variable de instancia self
        self.marca = "Huawei"

telefono = FabricaTelefonos()
marca1 = telefono.marca
print(marca1)
telefono.ElaborarHuawei()
print(telefono.marca)

class FabricaTelefonos1():
    #método contructor
    def __init__(self):
        print("Estoy ejecutando el método init, porque se ha creado un nuevo objeto")

Ntelefono = FabricaTelefonos1() #Se ejecuta el método init
Ntelefono2 = FabricaTelefonos1() #Se ejecuta el método init

class FabricaTelefonos2():
    #método contructor
    def __init__(self, marca, color, memoria, memoriaRam):
        self.marca = marca
        self.color = color
        self.memoria = memoria
        self.memoriaRam = memoriaRam


Telefono1 = FabricaTelefonos2("Samsung", "Gris", 8, 32)
print(f"Telefono marca: {Telefono1.marca}")
print(f"Telefono de color: {Telefono1.color}")

class PruebaLocal:
    def metodo_a(self):
        self.valor_local = 45 # Variable local
        return self.valor_local

    def metodo_b(self):
        try:
            return self.valor_local*3
        except NameError:
            return "valor_local no existe en el método_b"

Prueba = PruebaLocal()
print(Prueba.metodo_a())
print(Prueba.metodo_b())