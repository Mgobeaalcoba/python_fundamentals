# Cargar una lista con numeros al azar entre 1 y 100, donde la cantidad de elementos será ingresada por
# el usuario. Luego se solicita ingresar un valor y buscarlo en la lista informando su ubicación o -1 si
# no se lo encuentra.

import random

def cargarlista(cantidad):
    lista = []
    for i in range(cantidad):
        lista.append(random.randint(1,100))
        i = i + 1
    return lista

def imprimirlista(lista):
    for i in range(len(lista)):
        print(lista[i],end=" ")
    print()
    
def busquedasecuencial(lista,dato):  # Busqueda
    i = 0
    while i < len(lista) and lista[i] != dato:
        i = i + 1
    if i < len(lista):
        return i
    else:
        return -1

largo=int(input("Seleccione el largo de la lista a crear: "))
busqueda=int(input("Seleccione el numero que desea buscar en la lista: "))
milista=cargarlista(largo)
largolista=len(milista)

imprimirlista(milista)

subindice=busquedasecuencial(milista,busqueda)

if subindice == -1:
    print("\nNo se ha encontrado el numero buscado.")
else:
    print("El numero buscado se encuentra en el sub-indice:",subindice,"de la lista.")