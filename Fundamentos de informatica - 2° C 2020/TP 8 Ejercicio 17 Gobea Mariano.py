# Dada una lista ordenada de números llamada A y un nuevo número N, desarrollar un
# programa que agregue el elemento N dentro de la lista A, respetando el ordenamiento
# existente. El programa deberá detectar automáticamente si el ordenamiento es
# ascendente o descendente antes de realizar la inserción.

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
                
def detectarordenamiento(lista):  #Detecta orden ascendente o descendente
    tipo="ascendente"
    if lista[0] > lista[len(lista)-1]:
        tipo="descendente"
    return tipo

def imprimirlista(lista):
    largo=len(lista)
    for i in range(largo):
        print(lista[i],end=" ")
    print()
                
def agregarordenado(lista,dato,orden):
    if orden == "ascendente":
        i=0
        while dato > lista[i]:
            i=i+1
        lista.append(0)
        j=len(lista)-2
        for j in range(j,i-1,-1):
            lista[j+1]=lista[j]
        lista[i]=dato
            
    else:
        i=0
        while dato < lista[i]:
            i=i+1
        lista.append(0)
        j=len(lista)-2
        for j in range(j,i-1,-1):
            lista[j+1]=lista[j]
        lista[i]=dato 
        
    return lista 
    
# Programa Principal
A=cargarlista()
imprimirlista(A)
metododeseleccion(A)
ordenamiento=detectarordenamiento(A)
print("Lista ordenada de forma",ordenamiento,":")
imprimirlista(A)
N=int(input("Defina el elemento que desea sumar a la lista: "))
agregarordenado(A,N,ordenamiento)
print("Dato agregado en la lista.")
imprimirlista(A)






