
import random

def busquedabinaria(lista,dato):             # Selección
    izq = 0
    der = len(lista) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if lista[centro] == dato:
            pos = centro
        elif lista[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
    return pos

def metododeselección(lista):          # Ordenamiento
    largo = len(lista)
    for i in range(largo - 1):
        for j in range(i+1, largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

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

largo=int(input("Seleccione el largo de la lista a crear: "))
busqueda=int(input("Seleccione el numero que desea buscar en la lista: "))
milista=cargarlista(largo)
largolista=len(milista)

imprimirlista(milista)
metododeselección(milista)
print("Lista ordenada")
imprimirlista(milista)

subindice=busquedabinaria(milista,busqueda)

if subindice == -1:
    print("\nNo se ha encontrado el numero buscado.")
else:
    print("El numero buscado se encuentra en el sub-indice:",subindice,"de la lista.")

