# Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo
# la lista luego de invocar a cada función:
# a.Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos
# dígitos.
# b.Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
# c.Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la
# función lo recibe como parámetro.
# d.Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares. Un ejemplo de lista capicúa es
# [50, 17, 91, 17, 50].

import random

# Funciones:
def cargarlista():
    lista=[]
    elem=random.randint(10,99)
    for i in range (elem):
        lista.append(random.randint(1000,9999))
    return lista

def sumarlista(lista):
    sumatoria=sum(lista)
    return sumatoria

def eliminardelista(dato,lista):
    i = 0
    while i < len(lista):
        if dato in lista:
            lista.remove(dato)
        else:
            i += 1

def escapicua(lista):
    largo=(len(lista))
    capicua=True
    i = 0
    j = -1
    while capicua == True and i < largo:
        if lista[i] != lista[j]:
            capicua=False
        else:
            i += 1
            j -= 1
    return capicua

# Programa principal:

milista=cargarlista()
print(*milista,sep=" / ")
sumalista=sumarlista(milista)
print(sumalista)
eliminado=int(input("Seleccione que valor de la lista anterior desea eliminar: "))
valido= eliminado in milista
while valido == False:
    eliminado=int(input("El valor ingresado no se encuentra en la lista. Seleccione que valor de la lista anterior desea eliminar: "))
    valido= eliminado in milista
eliminardelista(eliminado,milista)
print(*milista,sep=" / ")
capi=escapicua(milista)
if capi == True:
    print("La lista es capicua")
else:
    print("La lista no es capicua")
    
        