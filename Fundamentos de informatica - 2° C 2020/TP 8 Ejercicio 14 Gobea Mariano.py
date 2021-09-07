# Ingresar 20 números e indicar cuales son los 5 mayores.

import random

def cargarlista():
    lista=[]
    LARGO=20
    for i in range(LARGO):
        lista.append(random.randint(0,100))
    return lista

def imprimirlista(lista):
    for i in range(len(lista)):
        print(lista[i],end=" ")
    print()
    
def imprimirmayores(lista):
    print("Los 5 numeros mayores de la lista son:",end=" ")
    for i in range(5):
        print(lista[i],end=" ")
    print()

def metododeseleccion(lista):   #Ordenamiento
    largo=len(lista)
    for i in range(largo-1):
        for j in range (i+1,largo):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
#Programa Principal

milista=cargarlista()
imprimirlista(milista)
metododeseleccion(milista)
print("Lista ordenada.")
imprimirmayores(milista)
