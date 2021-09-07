# Escribir un programa que utilice funciones para:
# Cargar una lista de N elementos con números enteros entre 50 y 780 obtenidos al azar.
# El valor de N se ingresa por teclado.
# Ordenar la lista en forma ascendente utilizando cualquier método de ordenamiento estudiado.
# Pedir un dato al usuario y buscarlo con búsqueda binaria e informar su posición o -1 sino se
# encuentra.
# Luego eliminar de la lista, el valor minimo en todas sus posiciones.
# Imprimir por pantalla la lista luego de realizar cada tarea.

# Modulos:

import random

# Funciones:

def cargarlista():      #Carga de lista
    lista=[]
    largo=int(input("Ingrese el largo de su lista: "))
    for i in range(largo):
        lista.append(random.randint(50,780)) 
    return lista
          
def metododeseleccion(lista):   #Ordenamiento
    largo=len(lista)
    for i in range(largo-1):
        for j in range (i+1,largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

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

def imprimirlista(lista):  #Imprimir lista
    largo=len(lista)
    for i in range(largo):
        print(lista[i],end=" ")
    print()
    
def eliminardelista(lista,dato):
    i=0
    while i < len(lista):
        if dato == lista[i]:
            del lista[i]
        else:
            i += 1
    return lista
    
# Programa Principal:

milista=cargarlista()
print("La lista original es:",end=" ")
imprimirlista(milista)
metododeseleccion(milista)
print("La lista ordenada de forma ascendente es:",end=" ")
imprimirlista(milista)
buscado=int(input("Ingrese un numero entre 50 y 780 que desee encontrar en la lista: "))
while buscado < 50 or buscado > 780:
    buscado=int(input("Recuerde que el numero a buscar debe estar entre el 50 y el 780. Intententelo nuevamente: "))
posicion=busquedabinaria(milista,buscado)
if posicion == -1:
    print("No se encontró el dato solicitado en la lista")
else:
    print("El dato solicitado se encuentra en el sub-índice:",posicion,".")
minimo=milista[0]  #Porque la lista ya está ordenada de forma ascendente
print("El mínimo de la lista es:",minimo)
eliminardelista(milista,minimo)
print("La lista sin el mínimo es:",end=" ")
imprimirlista(milista)

