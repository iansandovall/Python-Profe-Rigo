#Solicitar datos al usuario
#input
#variable = input("Mensaje a presentar en pantalla")

#para comentar todo un texto grande se usa triple compilla simple

'''
vocal= input("Escriba una vocal: ")
print(vocal)

#condicional es "if" si tal cosa cumple tal cosa has esto, es una condición que se aplica a traves de "if"
#sintáxis if condición:""
#if vocal.upper() == "E":
#    print("Has escrito la vocal E")

#Método booleano
cadena = input("Inserte un dato alfanumérico: ")
if cadena.isalnum():
    print("Has escrito una entrada valida")
else:
    print("Entrada inválida, intenta nuevamente")
    '''
email = input("Escribe tu email: ")
print(email.find("@"))
print(email.find("."))

if email.find("@") >= 4 and email.find(".") > 7:
    print("Tu email es válido")
else:
    print("Correo inválidp, intenta nuevamente")