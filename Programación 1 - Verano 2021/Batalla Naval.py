# 1 Portaaviones: ocupa 4 casillas
# 3 Submarinos: ocupan 3 casillas
# 3 Destructores: ocupan 2 casillas
# 2 Fragatas: ocupan 1 casilla

import random

# Funciones:

def crear_tableros():
    tablero=[['O']*10 for f in range(10)]
    return tablero

def imprimir_tablero(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    nombrefilas=["A","B","C","D","E","F","G","H","I","J"]
    nombrecolumnas=[numero for numero in range(1,11)]
    print(" ",end=" ")
    for n in nombrecolumnas:
        print(n,end=" ")
    print()
    for f in range(filas):
        print(nombrefilas[f],end=" ")
        for c in range(columnas):
            print(matriz[f][c],end="|")
        print()
        
def cargar_portaaviones(matriz):

    longporta=3
    nombrefilas=["A","B","C","D","E","F","G","H","I","J"]
    nombrecolumnas=[numero for numero in range(1,11)]
    orientaciones=["Arriba","Abajo","Izquierda","Derecha"]
    
    filaport=input("Seleccione la fila en la que desea ubicar su portaaviones entre la A y la J: ")
    filaport=filaport.upper()
    while filaport not in nombrefilas:
        filaport=input("La fila seleccionada no existe. Seleccione la fila en la que desea ubicar su portaaviones entre la A y la J: ")
        filaport=filaport.upper()
    filaport2=nombrefilas.index(filaport)
    
    while True:
        try:
            coluport=int(input("Seleccione la columna en la que desea ubicar su portaaviones entre la 1 y la 10: "))
            while coluport not in nombrecolumnas:
                coluport=int(input("Columna inexistente. Seleccione la columna en la que desea ubicar su portaaviones entre la 1 y la 10: "))
            coluport2=coluport-1
            print("Ya eleigió la ubicación de su portaviones. El mismo ocupa 4 lugares.")
            break
            
        except ValueError:
            print("Ingreso un valor incorrecto. Recuerde que la columna debe ser nombrada con un numero entre el 1 y el 10.")
                
    orienport=input("Seleccione ahora la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
    orienport=orienport.capitalize()
    while orienport not in orientaciones:
        orienport=input("Seleccione ahora la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
        orienport=orienport.capitalize()
    verificacion=False
    
    while verificacion == False:
        
        if orienport == "Arriba":
            arriba=filaport2-longporta
            if arriba < 0:
                verificacion=False
            else:
                verificacion=True
        elif orienport == "Abajo":
            abajo=filaport2+longporta
            if abajo > 9:
                verificacion=False
            else:
                verificacion=True
        elif orienport == "Izquierda":
            izquierda=coluport2-longporta
            if izquierda < 0:
                verificacion=False
            else:
                verificacion=True
        else:
            derecha=coluport2+longporta
            if derecha > 9:
                verificacion=False
            else:
                verificacion=True
                
        if verificacion == False:
            print("La orientación seleccionada no es valida ya que no entra en el tablero.")
            orienport=input("Seleccione ahora la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
            orienport=orienport.capitalize()
            while orienport not in orientaciones:
                orienport=input("Seleccione ahora la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
    
    if orienport == "Arriba":
        for f in range(filaport2,(filaport2-longporta-1),-1):
            matriz[f][coluport2]="X"
    elif orienport == "Abajo":
        for f in range(filaport2,(filaport2+longporta+1)):
            matriz[f][coluport2]="X"
    elif orienport == "Izquierda":
        for c in range(coluport2,(coluport2-longporta-1),-1):
            matriz[filaport2][c]="X"
    else:
        for c in range(coluport2,(coluport2+longporta+1)):
            matriz[filaport2][c]="X"
            
def cargar_submarinos(matriz):
    for i in range(3):
        longsub=2
        nombrefilas=["A","B","C","D","E","F","G","H","I","J"]
        nombrecolumnas=[numero for numero in range(1,11)]
        orientaciones=["Arriba","Abajo","Izquierda","Derecha"]
        
        filasub=input("Seleccione la fila en la que desea ubicar su submarino entre la A y la J: ")
        filasub=filasub.upper()
        while filasub not in nombrefilas:
            filasub=input("La fila seleccionada no existe. Seleccione la fila en la que desea ubicar su portaaviones entre la A y la J: ")
            filasub=filasub.upper()
        filasub2=nombrefilas.index(filasub)
            
        try:
            colusub=int(input("Seleccione la columna en la que desea ubicar su submarino entre la 1 y la 10: "))
            while colusub not in nombrecolumnas:
                colusub=int(input("Columna inexistente. Seleccione la columna en la que desea ubicar su submarino entre la 1 y la 10: "))
            colusub2=colusub-1
            print("Ya eleigió la ubicación de su submarino. El mismo ocupa 3 lugares.")
            
        except ValueError:
            print("Ingreso un valor incorrecto. Recuerde que la columna debe ser nombrada con un numero entre el 1 y el 10.")
                
        oriensub=input("Seleccione ahora la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
        oriensub=oriensub.capitalize()
        while oriensub not in orientaciones:
            oriensub=input("Seleccione ahora la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
            oriensub=oriensub.capitalize()
        verificacion=False
        
        while verificacion == False:
            
            if oriensub == "Arriba":
                arriba=filasub2-longsub
                if arriba < 0:
                    verificacion=False
                else:
                    verificacion=True
            elif oriensub == "Abajo":
                abajo=filasub2+longsub
                if abajo > 9:
                    verificacion=False
                else:
                    verificacion=True
            elif oriensub == "Izquierda":
                izquierda=colusub2-longsub
                if izquierda < 0:
                    verificacion=False
                else:
                    verificacion=True
            else:
                derecha=colusub2+longsub
                if derecha > 9:
                    verificacion=False
                else:
                    verificacion=True
                    
            if verificacion == False:
                print("La orientación seleccionada no es valida ya que no entra en el tablero.")
                oriensub=input("Seleccione ahora la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
                oriensub=oriensub.capitalize()
                while oriensub not in orientaciones:
                    oriensub=input("Seleccione ahora la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
        
        if oriensub == "Arriba":
            for f in range(filasub2,(filasub2-longsub-1),-1):
                matriz[f][colusub2]="X"
        elif oriensub == "Abajo":
            for f in range(filasub2,(filasub2+longsub+1)):
                matriz[f][colusub2]="X"
        elif oriensub == "Izquierda":
            for c in range(colusub2,(colusub2-longsub-1),-1):
                matriz[filasub2][c]="X"
        else:
            for c in range(colusub2,(colusub2+longsub+1)):
                matriz[filasub2][c]="X"
    
     
        
# Programa Principal:

tablerojuego1=crear_tableros()
tableroposicion1=crear_tableros()
tablerojuego2=crear_tableros()
tableroposicio2=crear_tableros()

imprimir_tablero(tablerojuego1)
cargar_portaaviones(tablerojuego1)
imprimir_tablero(tablerojuego1)
cargar_submarinos(tablerojuego1)
imprimir_tablero(tablerojuego1)