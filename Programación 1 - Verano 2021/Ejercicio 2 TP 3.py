# Para cada una de las siguientes matrices, desarrollar una función que la genere y escribir un programa que invoque
# a cada una de ellas y muestre por pantalla la matriz obtenida. El tamaño de las matrices debe establecerse como
# N x N, y las funciones deben servir aunque este valor se modifique.

def crearmatriza(filas,columnas):
    matriz=[]
    for f in range(filas):
        matriz.append([0]*columnas)
    ins=1
    for f in range(filas):
        for c in range(columnas):
            if f == c:
                matriz[f][c]=ins
                ins += 2
    return matriz

def crearmatrizf(filas,columnas):
    matriz=[]
    for f in range(filas):
        matriz.append([0]*columnas)
    aux=1
    c=-1
    for f in range(filas):
        while c >= columnas*-1:
            if abs(c) <= (f+1):
                matriz[f][c]=aux
                aux += 1
            c -= 1
        c = -1
    return matriz

def crearmatrizb(filas,columnas):
    matriz=[]
    for f in range(filas):
        matriz.append([0]*columnas)
    aux=1
    f= -1
    c= 1
    while f >= filas*-1:
        while (c-1) < columnas:
            if abs(f) == c:
                matriz[f][c-1]=aux
                aux *= 3
            c += 1
        c = 1
        f -= 1
    return matriz

def crearmatrizc(filas,columnas):
    matriz=[]
    for f in range(filas):
        matriz.append([0]*columnas)
    aux=4
    for f in range(filas):
        for c in range(columnas):
            if c <= f:
                matriz[f][c]=aux
        aux -= 1
    return matriz

def crearmatrizd(filas,columnas):
    matriz=[]
    for f in range(filas):
        matriz.append([0]*columnas)
    aux=8
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c]=aux
        aux = int(aux/2)
    return matriz

def crearmatrize(filas,columnas):
    matriz=[]
    for f in range(filas):
        matriz.append([0]*columnas)
    aux=1
    for f in range(filas):
        for c in range(columnas):
            if f%2 == 0:  #Si la fila es par
                if c%2 == 1:   #Si la columna es impar
                    matriz[f][c]=aux
                    aux += 1
            else:    #Si la fila es impar
                if c%2 == 0:   #Si la columna es par
                    matriz[f][c]=aux
                    aux += 1
    return matriz

def crearmatrizg(filas,columnas):
    matriz=[]
    for f in range(filas):
        matriz.append([0]*columnas)
    aux=1
    f=0
    c=0
    limitepos=columnas
    limiteneg=0
    while c <= (columnas/2):
        while c < limitepos:
            if matriz[f][c] == 0:
                matriz[f][c]=aux
                aux += 1
            c += 1
        c -= 1
        while f < limitepos:
            if matriz[f][c] == 0:
                matriz[f][c]=aux
                aux += 1
            f += 1
        f -= 1
        while c >= limiteneg:
            if matriz[f][c] == 0:
                matriz[f][c]=aux
                aux += 1
            c -= 1
        c += 1
        while f >= limiteneg:
            if matriz[f][c] == 0:
                matriz[f][c]=aux
                aux +=1
            f -= 1
        f += 1
        c += 1
        f += 1
        limitepos -= 1
        limiteneg += 1
    return matriz

# Programa principal:

N=int(input("Ingrese la cantidad de filas y columnas que tendrá su matriz NxN: "))

f=N
c=N

mimatriz=crearmatrizg(f,c)
print("Su matriz es:")
for i in range(f):
    print(mimatriz[i])
print()

