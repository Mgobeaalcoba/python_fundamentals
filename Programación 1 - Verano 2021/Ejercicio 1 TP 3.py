# Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento, imprimiendo
# la matriz luego de invocar a cada función:
# a. Cargar números enteros en una matriz de N x N, ingresando los datos desde teclado.
# b. Ordenar en forma ascendente cada una de las filas de la matriz.
# c. Intercambiar dos filas, cuyos números se reciben como parámetro.
# d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
# e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji) Intercambiar el contenido de una fila a una
# columna y viceversa
# f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como parámetro.
# g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
# h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
# i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
# j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo una lista con los números de las mismas.
# NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera sea el valor ingresado.

# Funciones:
        
def crearmatriz(filas,columnas):
    matriz = []
    for f in range (filas):
        matriz.append([0]*columnas)
    return matriz

def cargarmatriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range (filas):
        for c in range (columnas):
            n=int(input("Ingrese un numero a la matriz: "))
            matriz[f][c]=n
            
def ordenarfilas(matriz):
    filas=len(matriz)
    for f in range(filas):
        matriz[f].sort()
        
            
def interfilas(matriz,f1,f2):    #Intercambio muy dificil
    if f2 > f1:
        flotante=matriz.pop(f2)
        if f1 >= len(matriz):
            matriz.append(flotante)
        else:
            matriz.insert(f1,flotante)
        flotante2=matriz.pop(f1+1)
        if f2 >= len(matriz):
            matriz.append(flotante2)
        else:    
            matriz.insert(f2,flotante2)
    else:
        flotante=matriz.pop(f2)
        if f1 >= len(matriz):
            matriz.append(flotante)
        else:
            matriz.insert(f1,flotante)
        flotante2=matriz.pop(f1-1)
        if f2 >= len(matriz):
            matriz.append(flotante2)
        else:    
            matriz.insert(f2,flotante2)
            
def interfilas2(matriz,f1,f2):    # Intercambio facil
    flotante=matriz[f1].copy()
    matriz[f1]=matriz[f2].copy()
    matriz[f2]=flotante.copy()
    
def interfilas3(matriz,f1,f2):    # Intercambio muy facil
    matriz[f1],matriz[f2] = matriz[f2].copy(),matriz[f1].copy()
    
def intercolumnas(matriz,c1,c2):  # Intercambio de columnas facil
    filas=len(matriz)
    for f in range(filas):
        flotante=matriz[f][c1]
        matriz[f][c1]=matriz[f][c2]
        matriz[f][c2]=flotante

def trasponer(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    c=0
    for f in range(filas):
        while c < columnas:
            matriz[f][c],matriz[c][f] = matriz[c][f],matriz[f][c]
            c += 1
        c = f+1
        
def promediofila(matriz,f):
    elem=len(matriz[f])
    total=sum(matriz[f])
    prom=total/elem
    return prom

def shareimparcolumna(matriz,c):
    filas=len(matriz)
    columnas=len(matriz[0])
    total=filas
    impar=0
    for f in range(filas):
        if matriz[f][c]%2==1:
            impar += 1
    share=impar/total*100
    return share

def simetricaprincipal(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    sime=True
    c=0
    f=0
    while f < filas and sime==True:
        while c < columnas and sime==True:
            if matriz[f][c] != matriz [c][f]:
                sime=False
            c += 1
        f += 1
    return sime

def simetricasecundaria(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    sime=True
    c=0
    f=0
    dif=filas-1
    while f < filas and sime==True:
        while c < columnas and sime==True:
            if matriz[f][c] != matriz[f+dif][c+dif]:
                sime=False
            c += 1
            dif -= 1
        f += 1
        dif = filas-1-f
    return sime

def palindromos(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    f=0
    f2=filas-1
    palindromos=[]
    capi=True
    for c in range(columnas):
        while f < filas and capi == True:
            if matriz[f][c] != matriz[f2][c]:
                capi=False
            f += 1
            f2 -= 1
        if capi == True:
            for i in range(filas):
                palindromos.append(matriz[i][c])
    return palindromos
                
# Programa pricipal:

N=int(input("Ingrese la cantidad de filas y columnas que tendrá su matriz NxN: "))

f=N
c=N

mimatriz=crearmatriz(f,c)
print("Su matriz es:")
for i in range(f):
    print(mimatriz[i])
print()

cargarmatriz(mimatriz)
print()
print("Su matriz cargada es: ")
for i in range(f):
    print(mimatriz[i])
print()

ordenarfilas(mimatriz)
print("Su matriz con las filas ordenadas de forma ascendente: ")
for i in range(f):
    print(mimatriz[i])
print()

fila1=int(input("Ingrese la fila que desea intercambiar: "))
while fila1 >= len(mimatriz):
    fila1=int(input("Valor incorrecto. Ingrese la fila que desea intercambiar: "))
fila2=int(input("Ingrese con que otra fila desea hacerlo: "))
while fila2 >= len(mimatriz):
    fila2=int(input("Valor incorrecto. Ingrese con que otra fila desea hacerlo: "))
print("Su matriz con las filas intercambiadas es: ")
interfilas3(mimatriz,fila1,fila2)
for i in range(f):
    print(mimatriz[i])
print()

columna1=int(input("Ingrese la columna que desea intercambiar: "))
while columna1 >= len(mimatriz[0]):
    columna1=int(input("Valor incorrecto. Ingrese la fila que desea intercambiar: "))
columna2=int(input("Ingrese con que otra fila desea hacerlo: "))
while columna2 >= len(mimatriz[0]):
    columna2=int(input("Valor incorrecto. Ingrese con que otra columna desea hacerlo: "))
intercolumnas(mimatriz,columna1,columna2)
print("Su matriz con las columnas intercambiadas es: ")
for i in range(f):
    print(mimatriz[i])
print()

print("La matriz traspuesta se ve así: ")
trasponer(mimatriz)
for i in range(f):
    print(mimatriz[i])
print()

fila=int(input("Ingrese el numero de fila que desea calcular su promedio: "))
promedio=promediofila(mimatriz,fila)
print("El promedio de la fila",fila,"es de",promedio,".")
print()

columna=int(input("Ingrese el numero de columna que desea calcular el porcentaje de numeros impares en la misma: "))
porcentaje=shareimparcolumna(mimatriz,columna)
print("El porcentaje de elementos con valor impar en la columna",columna,"es de:",porcentaje,"%.")
print()

simeprin=simetricaprincipal(mimatriz)
if simeprin==True:
    print("La matriz es simétrica en relación a su diagonal principal.")
else:
    print("La matriz es asimétrica en relación a su diagonal principal.")

simesecu=simetricasecundaria(mimatriz)
if simesecu==True:
    print("La matriz es simétrica en relación a su diagonal secundaria.")
else:
    print("La matriz es asimétrica en relación a su diagonal secundaria.")
    
palin=palindromos(mimatriz)
print("La lista de numeros pertenecientes a columnas palíndromos es:",palin)
