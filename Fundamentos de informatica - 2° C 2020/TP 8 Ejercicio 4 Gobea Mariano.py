# En los siguientes ejercicios utilice una de las funciones anteriores para ingresar datos
# en una lista y luego resuelva:

# Desarrollar un algoritmo que permita mostrar una lista de enteros con sus valores a la
# mitad. Ejemplo: Lista [1,2,3,4], mostrar: 0.5 1.0 1.5 2.0. 

def cargarlista():
    lista = []
    n=int(input("Ingrese un numero entre 1 y 20 o -1 para finalizar la carga: "))
    while n == 0 or n < -1:
        n=int(input("Numero ingresado invalido. Ingrese un numero entre 1 y 20 o -1 para finalizar la carga: "))
    while n != -1:
        lista.append(n)
        n=int(input("Ingrese un numero entre 1 y 20 o -1 para finalizar la carga: "))
        while n == 0 or n < -1:
            n=int(input("Numero ingresado invalido. Ingrese un numero entre 1 y 20 o -1 para finalizar la carga: "))
    return lista

milista = cargarlista()
largo = len(milista)

for i in range(largo):
    print(milista[i]/2,end=" ")
print()

