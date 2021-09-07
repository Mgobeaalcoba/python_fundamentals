# Escribir funciones para:
# a.Generar una lista de 50 números aleatorios del 1 al 100.
# b.Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función no debe modificar
# la lista.
# c.Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original, sin importar el
# orden. Combinar estas tres funciones en un mismo programa.

import random

# funciones:

def crearlista():
    lista=[]
    for i in range (50):
        lista.append(random.randint(1,100))
    return lista

def buscarrepetidos(lista):
    repetido=False
    i=0
    tope=len(lista)
    while repetido == False and i != tope:
        cant=lista.count(lista[i])
        if cant >= 2:
            repetido = True
        else:
            repetido = False
        i += 1
    return repetido

def eliminarrepetidos(lista):
    tope=len(lista)
    lista2 = []
    for i in range (tope):
        cant=lista.count(lista[i])
        if cant == 1:
            lista2.append(lista[i])
    return lista2
           

            
# Programa pincipal:

milista=crearlista()
print(milista)

repeticion=buscarrepetidos(milista)
print(repeticion)

milista2=eliminarrepetidos(milista)
print(milista2)

