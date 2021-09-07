# Desarrolle un programa que permita realizar reservas en una sala de cine de barrio de N filas con M butacas por
# cada fila. Las filas se deberán referenciar con las letras desde la A y las butacas con los números desde el 1.
# Desarrollar  las siguientes funciones y utilizarlas en un mismo programa:
# mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas del cine por pantalla. Se deberá
# mostrar antes de que el usuario realice la reserva y se volverá a mostrar luego de la misma, con los estados
# actualizados.
# reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la matriz en caso de estar disponible
# dicha butaca. La función devolverá True/False si logró o no reservar la butaca.
# cargar_sala: recibirá una matriz como parámetro y la cargará con valores aleatorios para simular una sala con
# butacas ya reservadas.
# butacas_libres: Recibirá como parámetro la matriz y retornará cuántas butacas desocupadas hay en la sala.
# butacas_contiguas: Buscará la secuencia más larga de butacas libres contiguas en una misma fila y devolverá las
# coordenadas de inicio de la misma.

import random

def crear_sala(filas,butacas):
    matriz=[]
    for f in range(filas):
        matriz.append(["_"]*butacas)
    return matriz
        
def mostrar_butacas(matriz):
    filas=len(matriz)
    for f in range(filas):
        print(matriz[f])
    print()
    
def reservar(matriz,fila,butaca):
    reservaok=True
    if matriz[fila][butaca]=="X":
        reservaok=False
    else:
        matriz[fila][butaca]="X"
    return reservaok
         
def cargar_sala(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    opciones=["_","X"]
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c]=random.choice(opciones)

def butacas_libres(matriz):
    libre=0
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] == "_":
                libre += 1
    return libre

def butacas_contiguas(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    contiguas=0
    mayor=0
    mayores=[]
    posiciones=[] # Guarda los subindices de la columna donde inicia la mayor cantidad de butacas contiguas
    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] == "_":
                contiguas += 1
            else:
                if contiguas > mayor:
                    mayor=contiguas
                    posinicial = c - contiguas
                contiguas = 0
        if contiguas > mayor:
            mayor=contiguas
            posinicial= c - contiguas + 1
        contiguas = 0
        mayores.append(mayor)
        posiciones.append(posinicial)
    mayor2=max(mayores)
    filadelmayor=mayores.index(mayor2)
    columnadelmayor=posiciones[filadelmayor]
    return filadelmayor , columnadelmayor
                 
#Programa principal:
N=10  #Filas
M=5   #Butacas por fila
filascine=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
misfilas=filascine[ :N]
micine=crear_sala(N,M)

venta=True
modo=input("¿Desea encender en modo venta el programa? Debe responder \"si\" o \"no\": ")
while modo != "si" and modo != "no":
    modo=input("Respuesta incorrecta. ¿Desea encender en modo venta el programa? Debe responder \"si\" o \"no\": ")
if modo == "no":
    venta=False

# Modo ventas:

while venta == True:
    proximareserva=True
    print("Bienvenido a Gobea Cinemas. A continuación le mostraremos nuestra sala. Aquellas butacas que se encuentren ocupadas estarán identificadas con una letra X.")
    while proximareserva == True:
        mostrar_butacas(micine)
        print("Seleccione una fila donde ubicarse entre la A y la",misfilas[-1],":",end=" ")
        fila=input()
        while fila not in misfilas:
            print("La fila seleccionada no existe. Seleccione una fila donde ubicarse entre la A y la",misfilas[-1],":",end=" ")
            fila=input()
        print("Seleccione la butaca en la que desea sentarse dentro de la fila",fila,":",end=" ")
        butaca=int(input())-1
        while butaca >= M:
            print("La butaca seleccionada no existe. Seleccione la butaca en la que desea sentarse dentro de la fila",fila,":",end=" ")
            butaca=int(input())-1
        filaout=misfilas.index(fila)
        okreserva=reservar(micine,filaout,butaca)
        if okreserva == False:
            print("La butaca seleccionada se encuentra ocupada. Por favor vuelva a intentarlo.")
        else:
            print("Su reserva de butaca se realizó correctamente.")
        mostrar_butacas(micine)
        otrareserva=int(input("Presione 0 si desea realizar otra reserva o 1 si desea finalizar: "))
        while otrareserva != 1 and otrareserva != 0:
            otrareserva=int(input("Ingreso incorecto. Presione 0 si desea realizar otra reserva o 1 si desea finalizar: "))
        if otrareserva == 1:
            proximareserva = False
        else:
            proximareserva = True
    modo=input("¿Desea reservar entradas? Debe responder \"si\" o \"no\": ")
    while modo != "si" and modo != "no":
        modo=input("Respuesta incorrecta. ¿Desea reservar entradas? Debe responder \"si\" o \"no\": ")
    if modo == "no":
        venta=False

# Modo simulación:

print("A continuación se simulará el llenado de una sala de forma aleatoria: ")
cargar_sala(micine)
mostrar_butacas(micine)
repetir=int(input("Presione 1 si desea repetir la simulación o 0 si desea finalizar el programa: "))
while repetir != 0 and repetir != 1:
    repetir=int(input("Numero invalido. Presione 1 si desea repetir la simulación o 0 si desea finalizar el programa: "))
while repetir == 1:
    print("A continuación se simulará el llenado de una sala de forma aleatoria: ")
    cargar_sala(micine)
    mostrar_butacas(micine)
    repetir=int(input("Presione 1 si desea repetir la simulación o 0 si desea finalizar el programa: "))
    while repetir != 0 and repetir != 1:
        repetir=int(input("Numero invalido. Presione 1 si desea repetir la simulación o 0 si desea finalizar el programa: "))

vacios=butacas_libres(micine)
print("La cantidad de butacas libres es de:",vacios,".")
print()
coorfila , coorcolumna = butacas_contiguas(micine)
print("La secuencia mas larga de butacas libres en una misma fila de la sala comienza en la fila",misfilas[coorfila],"columna",(coorcolumna+1),".")