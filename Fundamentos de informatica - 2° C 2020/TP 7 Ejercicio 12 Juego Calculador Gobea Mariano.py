# Una calculadora tiene cuatro operaciones básicas (a saber: sumar, restar, multiplicar, dividir).
# Desarrolle una función para realizar cada operación, que reciba como parámetros dos números ingresados
# por el usuario y devuelva el resultado de la operación. Resuelva la división por restas sucesivas
# (investigar cómo se resuelve). Incluya un menú que permita realizar una operación y posea una opción
# para “Salir”. Luego de cada operación realizada se debe volver a presentar el menú.

#Funciones:

def sumar(a,b):
    resultado = a+b
    return resultado

def restar(a,b):
    resultado = a-b
    return resultado

def multiplicar(a,b):
    resultado = a*b
    return resultado

def dividir(a,b):
    contador=0
    resultado=a
    while resultado >= b:
        resultado = resultado - b
        contador += 1
    return contador

# Programa Principal

operación=input("¿Que operación desea realizar - Sumar, Restar, Dividir o Multiplicar -? o escriba Salir para terminar ")
while operación != "Sumar" and operación != "Restar" and operación != "Dividir" and operación != "Multiplicar" and operación != "Salir":
    operación=input("Operación seleccionada invalida. Seleccióne una de las siguientes opciones: Sumar, Restar, Dividir, Multiplicar o Salir: ")

while operación != "Salir":
    numero1=float(input("Ingrese el primer numero con el que desea operar: "))
    numero2=float(input("Ingrese el segundo numero con el que desea operar: "))
    if operación == "Sumar":
        result = sumar(numero1,numero2)
    elif operación == "Restar":
        result = restar(numero1,numero2)
    elif operación == "Multiplicar":
        result = multiplicar(numero1,numero2)
    else:
        result = dividir(numero1,numero2)
    print(result)
    operación=input("¿Que operación desea realizar - Sumar, Restar, Dividir o Multiplicar -? o escriba Salir para terminar ")
    while operación != "Sumar" and operación != "Restar" and operación != "Dividir" and operación != "Multiplicar" and operación !="Salir":
        operación=input("Operación seleccionada invalida. Seleccióne una de las siguientes opciones: Sumar, Restar, Dividir, Multiplicar o Salir: ")

if operación == "Salir":
    print("Fin del programa")
