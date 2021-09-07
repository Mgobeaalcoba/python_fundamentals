# En los siguientes ejercicios utilice una de las funciones anteriores para ingresar datos
# en una lista y luego resuelva:

# Crear tres listas y ordenarlas en forma ascendente utilizando un método para cada lista:
# métodos de selección, inserción y burbujeo. ¿Qué cambia para ordenar en forma descendente?
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

def metododeintercambio(lista): #Tambien llamado de burbujeo
    desordenado=True
    while desordenado:
        desordenado=False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                aux=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux
                desordenado=True

def metododeinsercion(lista):
    for i in range(1,len(lista)):
        aux=lista[i]
        j=i
        while j>0 and lista[j-1]>aux:
            lista[j]=lista[j-1]
            j=j-1
        lista[j]=aux

def imprimirlista(lista):
    largo=len(lista)
    for i in range(largo):
        print(lista[i],end=" ")
    print()
        
#Programa Principal

milista=cargarlista()
print("Lista 1 cargada.")
imprimirlista(milista)
milista2=cargarlista()
print("Lista 2 cargada.")
imprimirlista(milista2)
milista3=cargarlista()
print("Lista 3 cargada.")
imprimirlista(milista3)
print("\n")
metododeseleccion(milista)
metododeintercambio(milista2)
metododeinsercion(milista3)
imprimirlista(milista)
imprimirlista(milista2)
imprimirlista(milista3)