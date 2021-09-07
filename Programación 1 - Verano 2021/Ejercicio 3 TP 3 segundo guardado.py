# Desarrollar un programa para rellenar una matriz de N x N con números enteros al azar comprendidos en el intervalo
# [0,N2), de tal forma que ningún número se repita. Imprimir la matriz por pantalla.

import random

def crearmatriz(N):
    matriz=[]
    for f in range(N):
        matriz.append([0]*N)
    return matriz

def rellenarmatriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            repetido = True
            while repetido == True:
                numero=random.randint(0,filas**2)
                i = 0
                sigo = True
                while i < filas and sigo == True:
                    if numero in matriz[i]:
                        sigo = False
                    i += 1
                if sigo == True:
                    repetido = False
                    matriz[f][c] = numero
            
# Programa principal:

Numero=int(input("Ingrese el numero de filas y columnas que tendrá su matriz NxN: "))
mimatriz=crearmatriz(Numero)
print("Su matriz es:")
for i in range(Numero):
    print(mimatriz[i])
print()

rellenarmatriz(mimatriz)
print("Su matriz rellena con la regla planteada es: ")
for i in range(Numero):
    print(mimatriz[i])
print()



