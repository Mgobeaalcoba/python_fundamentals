# Diseñar una función para verificar si un número es par o impar, devolviendo True o False.
# Función

def verificar (numero):
    if numero % 2 == 0:
        par = True
    else:
        par = False
    return par

#Programa Principal

num=int(input("Ingrese el numero que desea verificar: "))
print("¿El numero ingresado es par?",verificar(num))
