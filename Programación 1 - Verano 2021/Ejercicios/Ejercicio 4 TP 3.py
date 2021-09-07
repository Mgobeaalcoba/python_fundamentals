# Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas en cada una de sus plantas
# durante una semana. De este modo, cada columna representa el día de la semana (Lunes columna 0, Martes columna 1…)
# y cada fila representa a una de sus fábricas.
# a.Crear una matriz con datos generados al azar de N fábricas durante una semana, considerando que la capacidad
# máxima de fabricación es de 150 unidades por día y puede suceder que en ciertos días no se fabrique ninguna.
# b.Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.
# c.Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
# d.Cuál es el día más productivo, considerando todas las fábricas combinadas.
# e.Crear una lista por comprensión que contenga la menor cantidad fabricada por cada fábrica.

import random

#Funciones:

def crearlista(filas):
    matriz=[]
    columnas=6
    for i in range(filas):
        matriz.append([0]*columnas)
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c]=random.randint(0,150)
    return matriz

def sumafabrica(matriz):
    sumas=[]
    filas=len(matriz)
    for f in range(filas):
        suma=sum(matriz[f])
        sumas.append(suma)
    return sumas

def maximaproduccion(matriz):
    filas=len(matriz)
    maximos=[]
    for f in range(filas):
        maximos.append(max(matriz[f]))
    maximo=max(maximos)
    for f in range(filas):
        if maximo in matriz[f]:
            fabrica=f
            dia=matriz[f].index(maximo)
    return maximo , fabrica , dia

def sumadia(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    producciondia=[]
    sumadiaria=0
    for c in range(columnas):
        for f in range(filas):
            sumadiaria = sumadiaria + matriz[f][c]
        producciondia.append(sumadiaria)
        sumadiaria=0
    diamax=producciondia.index(max(producciondia))
    return diamax , producciondia

def menorproduccion(matriz):
    filas=len(matriz)
    menores=[min(matriz[f]) for f in range(filas)]
    return menores
                      
# Programa principal:

n=int(input("Ingrese la cantidad de fabricas que tiene en producción: "))
mimatriz=crearlista(n)
print("Su matriz es: ")
for i in range(n):
    print(mimatriz[i])
print()

print("A continuación se detallará la suma semanal de lo producido por cada fabrica: ")
semanal=sumafabrica(mimatriz)
for i in range(n):
    print("El total producido en la semana por la fabrica",i+1,"es de:",semanal[i])
print()

dias = ["lunes","martes","miercoles","jueves","viernes","sabado"]
pico , fab , fecha = maximaproduccion(mimatriz)
print("El maximo de",pico,"fue logrado por la fabrica N°",fab+1,"el día",dias[fecha])
print()

diamaximo, totalesdiarios = sumadia(mimatriz)
print("El día de mayor producción sumando todas las fabricas fue el",dias[diamaximo])
print(totalesdiarios)
print()

minimos=menorproduccion(mimatriz)
print("Las menores cantidades producidas por cada fabrica en la semana son:")
print(minimos)
    