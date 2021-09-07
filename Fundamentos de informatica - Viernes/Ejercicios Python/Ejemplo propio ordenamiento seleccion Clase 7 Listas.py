# Cargar una lista con 100 numeros al azar entre 1 y 1000, imprimirla, ordenarla de menor
# a mayor y reimprimirla - Ordenar por metodo de selección
import random

def metododeselección(lista): # Ordenamiento
    largo = len(lista)
    for i in range(largo - 1):
        for j in range(i+1, largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
def cargarlista(largo):
    lista = []
    for i in range(largo):
        lista.append(random.randint(1,1000))
    return lista

def imprimirlista(lista):
    for i in range(len(lista)):
        print(lista[i],end=" ")
    print()
    
# Programa principal:
CANTIDAD=100
milista = cargarlista(CANTIDAD)
imprimirlista(milista)
metododeselección(milista)
print("Lista ordenada de menor a mayor.")
imprimirlista(milista)

