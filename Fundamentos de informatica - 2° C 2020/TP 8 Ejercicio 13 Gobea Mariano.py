# En los siguientes ejercicios utilice una de las funciones anteriores para ingresar datos
# en una lista y luego resuelva:

# Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar e imprimir el valor
# mínimo y el lugar que ocupa. Tener en cuenta que el mínimo puede estar repetido, en cuyo
# caso deberán mostrarse todas las posiciones que ocupe. La carga de datos termina cuando se
# obtenga un 0 como número al azar, el que no deberá cargarse en la lista.

import random

def cargarlista():
    lista=[]
    n=random.randint(0,100)
    while n != 0:
        lista.append(n)
        n=random.randint(0,100)
    return lista

def buscarminimo(lista):
    minimo=len(lista)+1
    for i in range(len(lista)):
        if milista[i] < minimo:
            minimo=milista[i]
    return minimo
            
def imprimirminimos(lista,minimo):
    for i in range(len(lista)):
        if lista[i] == minimo:
            print("El minimo es:",minimo,"y se encuentra en la posición:",i,".")

def imprimirlista(lista):
    largo=len(lista)
    for i in range(largo):
        print(lista[i],end=" ")
    print()
    
#Programa Principal
    
milista=cargarlista()
imprimirlista(milista)
minimo=buscarminimo(milista)
imprimirminimos(milista,minimo)
          
            
    