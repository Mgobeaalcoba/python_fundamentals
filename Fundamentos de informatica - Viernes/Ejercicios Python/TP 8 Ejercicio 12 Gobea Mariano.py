# En los siguientes ejercicios utilice una de las funciones anteriores para ingresar datos
# en una lista y luego resuelva:

# Utilizando búsqueda binaria sobre una lista ordenada realizar la búsqueda de valores e
# informar si se encuentran o no en la lista, finalizar las búsquedas con -1 e informar
# cuantas búsquedas fueron exitosas y en cuantas no se encontró el valor buscado.

import random

def cargarlista():
    lista=[]
    n=int(input("Defina el largo de la lista: "))
    minimo=int(input("Defina el minimo de la lista: "))
    maximo=int(input("Defina el maximo de la lista: "))
    for i in range(n):
        lista.append(random.randint(minimo,maximo))
    return lista

def metododeseleccion(lista):
    largo=len(lista)
    for i in range(largo-1):
        for j in range (i+1,largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
def busquedabinaria(lista,dato):
    izq=0
    der=len(lista)-1
    pos=-1
    while izq<=der and pos==-1:
        centro=(izq+der)//2
        if lista[centro]==dato:
            pos=centro
        elif lista[centro]<dato:
            izq=centro+1
        else:
            der=centro-1
    return pos

def imprimirlista(lista):
    largo=len(lista)
    for i in range(largo):
        print(lista[i],end=" ")
    print()

# Utilizando búsqueda binaria sobre una lista ordenada realizar la búsqueda de valores e
# informar si se encuentran o no en la lista, finalizar las búsquedas con -1 e informar
# cuantas búsquedas fueron exitosas y en cuantas no se encontró el valor buscado.

milista=cargarlista()
metododeseleccion(milista)
imprimirlista(milista)
n=int(input("Ingrese el numero que desea buscar o -1 para terminar: "))
exito=0
fracaso=0
while n != -1:
    posicion=busquedabinaria(milista,n)
    if posicion != -1:
        exito=exito+1
        print("La busqueda fue exitosa. El numero indicado se encuentra en la posición:",posicion)
    else:
        fracaso=fracaso+1
        print("Busqueda fallida. El numero solicitado no se encuentra en la lista.")
    n=int(input("Ingrese el numero que desea buscar o -1 para terminar: "))

print("La cantidad de busquedas exitosas es de:",exito,". Y la cantidad de busquedas fallidas es de:",fracaso)

    

