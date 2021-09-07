# En los siguientes ejercicios utilice una de las funciones anteriores para ingresar datos
# en una lista y luego resuelva:

# Cargar una lista con números aleatorios y reemplazar un valor en una posición
# determinada por el usuario.

import random
def cargarlista(largo):
    lista = []
    n1=int(input("Ingrese el minimo del rango: "))
    n2=int(input("Ingrese el maximo del rango: "))
    for i in range(largo):
        lista.append(random.randint(n1,n2))
    return lista

def reemplazarsubindice(lista):
    largo=len(lista)
    sub=int(input("Seleccione el numero de sub-indice que desea reemplazar: "))
    while sub > largo-1 or sub < 0:
        print("Valor ingresado invalido. El numero seleccionado debe estar entre: 0 y",largo-1,".",end=" ")
        sub=int(input())
    valor=int(input("Seleccione el numero que va a reemplazar al actual: "))
    lista[sub] = valor
    return lista

def imprimirlista(lista):
    for i in range(len(lista)):
        print(lista[i],end=" ")
    print()

# Programa principal

tamaño=int(input("Seleccione el largo de la lista: "))
milista=cargarlista(tamaño)
imprimirlista(milista)
reemplazarsubindice(milista)
imprimirlista(milista)

