# Ingresar números hasta ingresar -1. Informar cuántos números pares se ingresaron y su suma.
# Utilizar la función del ejercicio 7 para resolverlo.

# Funciones

def verificar (numero):
    if numero % 2 == 0:
        par = True
    else:
        par = False
    return par

# Programa Principal

num=int(input("Ingrese un numero o -1 para terminar: "))
contador=0
acumulador=0
while num != -1:
    if verificar(num) == True:
        contador += 1
        acumulador = acumulador + num
    num=int(input("Ingrese un numero o -1 para terminar: "))
        
print("Se ingresaron:",contador,"numeros pares y su suma es igual a:",acumulador,".")


