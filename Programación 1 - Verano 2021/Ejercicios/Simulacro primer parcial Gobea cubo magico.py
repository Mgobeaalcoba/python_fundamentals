# Escribir un programa para cargar valores en una matriz de N x N(con N ingresado por el usuario o generado al azar) e
# imprimir un mensaje indicando si se trata de un cuadrado mágico o no. Si lo es, mostrar su suma mágica. Imprimir tambien
# la matriz utilizada.

import random

# Funciones:
def crear_matriz(N):
    matriz=[]
    for f in range(N):
        matriz.append([0]*N)
    for f in range(N):
        for c in range(N):
            matriz[f][c]=int(input("Ingrese un numero a su matriz: "))
    return matriz

def imprimir_matriz(matriz):
    filas=len(matriz)
    for f in range(filas):
        print(matriz[f])
        
def cuadro_magico(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    magico=False
    aux=0
    aux2=0
    for f in range(filas-1):
        for c in range(columnas):
            aux=aux+matriz[f][c]
            aux2=aux2+matriz[f+1][c]
        if aux == aux2:
            magico=True
            aux=0
            aux2=0
        else:
            break
    if magico==True:
        for c in range(columnas-1):
            for f in range(filas):
                aux=aux+matriz[f][c]
                aux2=aux2+matriz[f][c+1]
            if aux == aux2:
                aux=0
                aux2=0
            else:
                magico=False
                break
    if magico==True:
        j=columnas-1
        for i in range(filas):
            aux=aux+matriz[i][i]
            aux2=aux2+matriz[i][j]
            j -= 1
        if aux != aux2:
            magico=False
    return magico
                
# Programa principal:
n=random.randint(2,6)
mimatriz=crear_matriz(n)
imprimir_matriz(mimatriz)
esmagico=cuadro_magico(mimatriz)
if esmagico == True:
    sumamagica=sum(mimatriz[0])
    print("Se trata de un cuadro magico.")
    print("Su suma mágica es:",sumamagica,".")
else:
    print("No se trata de una suma magica")
