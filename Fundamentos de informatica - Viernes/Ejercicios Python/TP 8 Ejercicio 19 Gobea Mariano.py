# Leer dos listas de números M y N, ambas ordenadas de menor a mayor. Generar e imprimir una
# tercera lista que resulte de intercalar los elementos de M y N. La nueva lista también debe
# quedar ordenada, sin utilizar ningún método de ordenamiento.

import random
def cargarlista():
    lista=[]
    n=int(input("Defina el largo de la lista: "))
    minimo=int(input("Defina el minimo de la lista: "))
    maximo=int(input("Defina el maximo de la lista: "))
    for i in range(n):
        lista.append(random.randint(minimo,maximo))
    return lista

def metododeseleccion(lista):   #Ordenamiento
    largo=len(lista)
    for i in range(largo-1):
        for j in range (i+1,largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
def combinarlistasordenadas(lista1,lista2):
    
    return lista3
                
# Programa Principal
M=cargarlista()
N=cargarlista()
