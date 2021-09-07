# Eliminar de una lista de números enteros los valores que se encuentren en una
# segunda lista. Mostrar la lista original, la lista de valores a eliminar y
# como queda la lista original luego de eliminar los valores.

import random
def cargarlista():
    lista=[]
    n=int(input("Defina el largo de la lista: "))
    minimo=int(input("Defina el minimo de la lista: "))
    maximo=int(input("Defina el maximo de la lista: "))
    for i in range(n):
        lista.append(random.randint(minimo,maximo))
    return lista

def eliminardelista(lista1,lista2):   #Eliminar una lista de otra
    largo=len(lista1)
    j=0
    while j < len(lista2)-1:
        i=0
        while i < len(lista1)-1 and lista2[j] != lista1[i]:
            i = i + 1
        if i < len(lista1)-1:
            del lista1[i]
            j=j-1
        j=j+1
            
          
def imprimirlista(lista):
    largo=len(lista)
    for i in range(largo):
        print(lista[i],end=" ")
    print()
    
# Programa Principal

milista=cargarlista()
milista2=cargarlista()
imprimirlista(milista)
imprimirlista(milista2)
eliminardelista(milista,milista2)
print("Eliminamos el contenido de la segunda lista de la primera.")
imprimirlista(milista)


            