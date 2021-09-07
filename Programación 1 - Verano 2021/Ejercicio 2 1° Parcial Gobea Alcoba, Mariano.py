# Cargar una matriz de N x N elementos con números enteros, ingresados por teclado o generados al azar (desarrollar una
# sola de estas dos opciones). El valor de N se ingresa por teclado. Mostrar por pantalla la matriz obtenida. Luego se
# solicita informar:
# . Valor y ubicación del mayor elemento de la matriz.
# . Valor y ubicación de los elementos mayoy y menor de la diagonal secundaria.

# Módulos:

import random

# Funciones:

def crear_matriz(N):
    """ Crea una matriz N x N. """
    matriz=[[0]*N for i in range(N)]
    return matriz

def cargar_matriz(matriz):
    """ Carga la matriz enviada con
    numeros aleatorios entre 1 y 999. """
    filas=len(matriz)
    columnas=len(matriz[0])   #Podría omitirse ya que la matriz es N x N. Es decir, tiene igual cant de filas que de columnas
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c]=random.randint(1,999)
            
def imprimir_matriz(matriz):
    """ Imprime la matriz enviada con un
    espacio de lugares para cada elemento. """ 
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c],end=" ")
        print()
        
def calcular_mayor(matriz):
    """ Calcula el mayor numero de la
    matriz enviada, asi como su ubicación
    en fila y columna. """
    filas=len(matriz)
    mayores=[]
    columnas=[]
    for f in range(filas):
        maximo=max(matriz[f])
        columna=matriz[f].index(maximo)
        mayores.append(maximo)
        columnas.append(columna)
    maximo=max(mayores)
    fila=mayores.index(maximo)
    columna=columnas[fila]
    return maximo , fila , columna

def analizar_secundaria(matriz):
    """ Calcula el máximo y el minimo
    entre los valores introducidos en
    la diagonal secundaria de la matriz. """
    secundaria=[]
    filas=len(matriz)
    columnas=len(matriz[0])
    c=columnas-1
    for f in range(filas):
        secundaria.append(matriz[f][c])
        c -= 1
    maximo=max(secundaria)
    minimo=min(secundaria)
    return maximo , minimo

# Programa principal:

n=int(input("Ingrese el largo y ancho que desea para su matriz N x N: "))
mimatriz=crear_matriz(n)
cargar_matriz(mimatriz)
print()
imprimir_matriz(mimatriz)
maxi , fil , col = calcular_mayor(mimatriz)
print()
print("El mayor valor de la matriz es",maxi,"y se encuentra en la fila",fil,"columna",col,".")
maxsecu , minsecu = analizar_secundaria(mimatriz)
print()
print("El mayor numero de la diagonal secundaria es",maxsecu,"y el menor de la misma es",minsecu,".") 
