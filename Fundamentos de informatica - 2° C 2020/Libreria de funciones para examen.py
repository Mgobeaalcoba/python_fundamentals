# Libreria de funciones para examen

# Importante sobre ciclo While con condiciones anidadas: Cuando las condiciones están unidas con
# un "and" deben darse todas las condiciones unidas de esa manera para que se ingrese en el ciclo
# si están unidas con un "or" solo debe darse una de ellas para ingresar al ciclo. No ingresa si
# no se cumple ninguna de ellas. 

import random

def cargarlista():
    lista=[]
    n=int(input("Defina el largo de la lista: "))
    minimo=int(input("Defina el minimo de la lista: "))
    maximo=int(input("Defina el maximo de la lista: "))
    for i in range(n):
        lista.append(random.randint(minimo,maximo))
    return lista

def cargarlista2():  #Carga lista con corte random
    lista=[]
    n=random.randint(0,100)
    while n != 0:
        lista.append(n)
        n=random.randint(0,100)
    return lista

def imprimirlista(lista):
    largo=len(lista)
    for i in range(largo):
        print(lista[i],end=" ")
    print()

def metododeseleccion(lista):   #Ordenamiento
    largo=len(lista)
    for i in range(largo-1):
        for j in range (i+1,largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def metododeintercambio(lista): #Tambien llamado de burbujeo   #Ordenamiento
    desordenado=True
    while desordenado:
        desordenado=False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                aux=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux
                desordenado=True

def metododeinsercion(lista):     #Ordenamiento
    for i in range(1,len(lista)):
        aux=lista[i]
        j=i
        while j>0 and lista[j-1]>aux:
            lista[j]=lista[j-1]
            j=j-1
        lista[j]=aux
        
def busquedasecuencial(lista,buscado):   #Busqueda
    largo=len(lista)
    i = 0
    posicion = -1
    while i < largo and buscado != lista[i]:
        i = i + 1
    if i < largo:
        posicion = i
    else:
        posicion = -1
    return posicion

def busquedabinaria(lista,dato):    #Busqueda
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

