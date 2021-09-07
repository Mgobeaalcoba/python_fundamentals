#funciones 
import random

def crear_tableros():
    '''crea un tablero de 10x10 vacio'''
    tablero=[['O']*10 for f in range(10)]
    return tablero

def imprimir_tablero(matriz):
    '''imprime el tablero de manera grafica'''
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

def limpiar_pantalla(registro=0):
    '''limpia la pantalla de la consola de manera recursiva'''
    if registro < 20:
        limpiar_pantalla(registro+1)
        print()

def crear_archivo():
    '''crea archivo .txt con las normas de juego'''
    try:
        arch = open("BatallaNaval_Reglas.txt","wt")
        titulo = 'BATALLA NAVAL'
        arch.write(titulo.center(110,'-'))
        arch.write(' \n')
        arch.write(' \n')
        arch.write('Objetivo del juego:\n')
        arch.write(' \n')
        objetivo =  '''Hundir los 9 barcos de tu oponente antes que el acabe con los tuyos.\n Este juego correspone a una version Trial por lo que cada Jugador tiene \nun total de 15 turnos para realizar moviemientos a la hora de atacar. \nCada jugador tiene 2 tableros compuesto por 10 filas y 10 columnas. \n
        Tablero de posicion: es tu territorio, en este distribuiras tu flota antes de comenzar la partida. \nVeras la posicion de tus barcos y los disparos de tu oponente en tu territorio,\npero no podras realizar ningun cambio ni disparo en este.\n
        Tablero principal: es el territorio de tu enemigo, donde tiene desplegada su flota.\nSera aqui donde se desarrollen tus movimientos (disparos)y trataras de hundir los barcos enemigos.\nAparecera en tu pantalla una vez comience la partida y en el quedaran registrados todos tus movimientos,\nreflejando tanto los disparos al agua como los barcos hundidos hasta el momento.\n'''
        arch.write(objetivo)
        arch.write(' \n')
        arch.write('Ilustacion del tablero')
        arch.write(' \n')
        arch.write('  1 2 3 4 5 6 7 8 9 10 \n')
        arch.write('A O|O|O|O|O|O|O|O|O|O| \n')
        arch.write('B O|O|O|O|O|O|O|O|O|O| \n')
        arch.write('C O|O|O|O|O|O|O|O|O|O| \n')
        arch.write('D O|O|O|O|O|O|O|O|O|O| \n')
        arch.write('E O|O|O|O|O|O|O|O|O|O| \n')
        arch.write('F O|O|O|O|O|O|O|O|O|O| \n')
        arch.write('G O|O|O|O|O|O|O|O|O|O| \n')
        arch.write('H O|O|O|O|O|O|O|O|O|O| \n')
        arch.write('I O|O|O|O|O|O|O|O|O|O| \n')
        arch.write('J O|O|O|O|O|O|O|O|O|O| \n')
        arch.write(' \n')
        arch.write('La flota de barcos debe ser colocada en cada casillero representado por los "O"\n')
        arch.write(' \n')
        arch.write('- '*70)
        arch.write(' \n')
        arch.write(' \n')
        flota = '''Cada jugador cuanta con una flota de:  \n- 1 Portaaviones (4 casillas) X X X X  \n- 2 Submarinos (3 casillas) X X X\n- 3 Destructores (2 casillas) X X  \n- 4 Fragatas (1 casilla) X X X X
        \nLos mismos deberan ser colocados dentro del tablero previamente a comenzar el juego. \nSe pide ingresar la posicion y la oreintacion de los barcos (Arriba, Abajo, Izquierda o Derecha) \na la hora de colocarlos.'''
        arch.write(flota)
    except FileNotFoundError as mensaje:
        print('No se puede abrir el archivo',mensaje)
    except OSError as mensaje:
        print('No se puede leer el archivo',mensaje)
    finally:
        try:
            arch.close()
        except OSError:
            pass

def limpiar_pantalla_turnos():
    '''limpia pantalla para los turnos'''
    registro = 1
    while registro <= 5:
        print()
        registro += 1
    print('-'*80)
    registro = 1
    while registro <= 5:
        print()
        registro += 1


#funciones carga de barco

#portaaviones
def cargar_portaaviones(matriz):
    '''carga en el tablero el  de tipo portaaviones'''
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
            print("Ya eligió la ubicación de su portaviones. El mismo ocupa 4 lugares.")
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
                orienport=orienport.capitalize()
    
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

#submarino
def cargar_submarinos(matriz):
    '''carga en el tablero los barcos de tipo submarino'''
    submarinos = 3
    longsubma = 2
    for i in range (3):
        disponible = False
        while disponible == False:
            nombrefilas=["A","B","C","D","E","F","G","H","I","J"]
            nombrecolumnas=[numero for numero in range(1,11)]
            orientaciones=["Arriba","Abajo","Izquierda","Derecha"]
            filaport=input("Seleccione la fila en la que desea ubicar su submarino entre la A y la J: ")
            filaport=filaport.upper()
            while filaport not in nombrefilas:
                filaport=input("La fila seleccionada no existe. Seleccione la fila en la que desea ubicar su submarino entre la A y la J: ")
                filaport=filaport.upper()
            filaport2=nombrefilas.index(filaport)
            coluport=int(input("Seleccione la columna en la que desea ubicar su submarino entre la 1 y la 10: "))
            while coluport not in nombrecolumnas:
                coluport=int(input("Columna inexistente. Seleccione la columna en la que desea ubicar su submarino entre la 1 y la 10: "))
            coluport2=coluport-1
            
            #verificar posicion asignada se encuentra disponible
            if matriz[filaport2][coluport2] != "X":
                    disponible = True
            if disponible == True:
                print('Ubicacion disponible')
            else:
                print('Ubicacion no dispobile')

            if disponible == True:
                print("Ya eligió la ubicación de su submarino. El mismo ocupa 3 lugares.")
                orienport=input("Seleccione ahora la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
                orienport=orienport.capitalize()
                while orienport not in orientaciones:
                    orienport=input("Seleccione ahora la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
                    orienport=orienport.capitalize()
                #Verificacion de espacio y colocacion del submarino
                verificacion=False 
                while verificacion == False:
                    if orienport == "Arriba":
                        arriba=filaport2-longsubma
                        if arriba < 0 or matriz[filaport2-1][coluport2]=="X" or matriz[filaport2-2][coluport2]=="X":
                            verificacion=False
                        else:
                            verificacion=True
                            if verificacion == True and orienport == "Arriba":
                                for i in range(submarinos):
                                    matriz[filaport2][coluport2] = "X"
                                    filaport2 = filaport2 - 1              
                    elif orienport == "Abajo":
                        abajo=filaport2+longsubma
                        if abajo > 9 or matriz[filaport2+1][coluport2]=="X" or matriz[filaport2+2][coluport2]=="X":
                            verificacion=False
                        else:
                            verificacion=True
                            if verificacion == True and orienport == "Abajo":
                                for i in range(submarinos):
                                    matriz[filaport2][coluport2] = "X"
                                    filaport2 = filaport2 + 1
                    elif orienport == "Izquierda":
                        izquierda=coluport2-longsubma
                        if izquierda < 0 or matriz[filaport2][coluport2-1]=="X" or matriz[filaport2][coluport2-2]=="X":
                            verificacion=False
                        else:
                            verificacion=True
                            if verificacion == True and orienport == "Izquierda":
                                for i in range(submarinos):
                                    matriz[filaport2][coluport2] = "X"
                                    coluport2 = coluport2 - 1   
                    else:
                        derecha=coluport2+longsubma
                        if derecha > 9 or matriz[filaport2][coluport2+1]=="X" or matriz[filaport2][coluport2+2]=="X":
                            verificacion=False
                        else:
                            verificacion=True
                            if verificacion == True and orienport == "Derecha":
                                for i in range(submarinos):
                                    matriz[filaport2][coluport2] = "X"
                                    coluport2 = coluport2 + 1

                    if verificacion == False:
                        print("La orientación seleccionada no es valida ya que no entra en el tablero. O existen lugares ocupados por otros barcos")
                        orienport=input("Seleccione nuevamente la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
                        orienport=orienport.capitalize()
                        while orienport not in orientaciones:
                            orienport=input("Seleccione ahora la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
                            orienport=orienport.capitalize()
                    print()
    
#destructor
def cargar_destructor(matriz):
    '''carga en el tablero los barcos de tipo destructor'''
    longdest=1 #1 espacio mas el asignado por usuario
    llenado = 'X' #espacio de tablero ya ocupado por barco
    nombrefilas=["A","B","C","D","E","F","G","H","I","J"]
    nombrecolumnas=[numero for numero in range(1,11)]
    cantidadbarco = 3
    filas=len(matriz)
    columnas=len(matriz[0])

    for i in range (3): #debo ubicar 3 barcos
        disponible = False
        while disponible == False:
            #seleccionar fila
            filadest=input("Seleccione la fila en la que desea ubicar su Destructor entre la A y la J: ")
            filadest=filadest.upper()
            while filadest not in nombrefilas:
                filadest=input("La fila seleccionada no existe. Seleccione la fila en la que desea ubicar su Destructor entre la A y la J: ")
                filadest=filadest.upper()
            filadest2=nombrefilas.index(filadest) #posicion fila
            #seleccionar columna
            while True:
                try:
                    coludest=int(input("Seleccione la columna en la que desea ubicar su Destructor entre la 1 y la 10: "))
                    while coludest not in nombrecolumnas:
                        coludest=int(input("Columna inexistente. Seleccione la columna en la que desea ubicar su Destructor entre la 1 y la 10: "))
                    coludest2=coludest-1 #posicion columna
                    break
                except ValueError:
                    print("Ingreso un valor incorrecto. Recuerde que la columna debe ser nombrada con un numero entre el 1 y el 10.")

            #verificar posicion asignada se encuentra disponible
            if matriz[filadest2][coludest2] != llenado:
                disponible = True #ubicacion correcta, continuo la carga
            if disponible == True:
                print('Ubicacion disponible')
            else:
                print('Ubicacion no dispobile')
            
        #ingresar ubicacion
        print("Ya eligio la ubicación de su Destructor. El mismo ocupa 2 lugares.")
        orientaciones=["Arriba","Abajo","Izquierda","Derecha"]
        orienport=input("Seleccione ahora la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
        orienport=orienport.capitalize()
        while orienport not in orientaciones:  #verifico ubicaicon correcta
            orienport=input("Seleccione ahora la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
            orienport=orienport.capitalize()
        verificacion=False
        #verficaicon si entra por longuitud
        while verificacion == False:
            if orienport == "Arriba":
                arriba=filadest2-longdest
                if arriba < 0 or matriz[filadest2-1][coludest2]=="X" or matriz[filadest2-2][coludest2]=="X":
                    verificacion=False
                else:
                    for f in range(filas):
                        for c in range(columnas):
                            if matriz[filadest2-1][coludest2] == llenado:
                                verificacion = False
                                break
                            else:
                                verificacion = True
            elif orienport == "Abajo":
                abajo=filadest2+longdest
                if abajo > 9 or matriz[filadest2+1][coludest2]=="X" or matriz[filadest2+2][coludest2]=="X":
                    verificacion=False
                else:
                    for f in range(filas):
                        for c in range(columnas):
                            if matriz[filadest2+1][coludest2] == llenado:
                                verificacion = False
                                break
                            else:
                                verificacion = True
            elif orienport == "Izquierda":
                izquierda=coludest2-longdest
                if izquierda < 0 or matriz[filadest2][coludest2-1]=="X" or matriz[filadest2][coludest2-2]=="X":
                    verificacion=False
                else:
                    for f in range(filas):
                        for c in range(columnas):
                            if matriz[filadest2-1][coludest2] == llenado:
                                verificacion = False
                                break
                            else:
                                verificacion = True
            elif orienport == "Derecha": 
                derecha=coludest2+longdest
                if derecha > 9 or matriz[filadest2][coludest2+1]=="X" or matriz[filadest2][coludest2+2]=="X": #derecha
                    verificacion=False
                else:
                    for f in range(filas):
                        for c in range(columnas):
                            if matriz[filadest2+1][coludest2] == llenado:
                                verificacion = False
                                break
                            else:
                                verificacion = True
            if verificacion == False:
                print("La orientación seleccionada no es valida ya que no entra en el tablero. O existen lugares ocupados por otros barcos")
                orienport=input("Seleccione nuevamente la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
                orienport=orienport.capitalize()
                while orienport not in orientaciones: #verifico ubicaicon correcta
                    orienport=input("Seleccione ahora la orientación sobre la que se extenderá el mismo - Arriba, Abajo, Izquierda o Derecha: ")
                    orienport=orienport.capitalize()   

        barco = False
        if orienport == 'Arriba':
            for f in range(filadest2,(filadest2-longdest-1),-1):
                matriz[f][coludest2] = 'X'
                barco = True
        elif orienport == 'Abajo':
            for f in range(filadest2,(filadest2+longdest+1)):
                matriz[f][coludest2] = 'X'
                barco = True
        elif orienport == 'Izquierda':
            for c in range(coludest2,(coludest2-longdest-1),-1):
                matriz[filadest2][c] = 'X'
                barco = True
        else:
            for c in range(coludest2,(coludest2+longdest+1)):
                matriz[filadest2][c] = 'X'
                barco = True
            

        if barco == True:
            print('Barco cargado')
        else: 
            print('Error')
        print()
    
#fragata
def cargar_fragata(matriz):
    '''carga en el tablero los barcos de tipo Fragata'''
    llenado = 'X' #espacio de tablero ya ocupado por barco
    nombrefilas=["A","B","C","D","E","F","G","H","I","J"]
    nombrecolumnas=[numero for numero in range(1,11)]

    for i in range (2): #debo ubicar 2 barcos
        disponible = False
        while disponible == False:
            #seleccionar fila
            filafrag=input("Seleccione la fila en la que desea ubicar su Fragata entre la A y la J: ")
            filafrag=filafrag.upper()
            while filafrag not in nombrefilas:
                filafrag=input("La fila seleccionada no existe. Seleccione la fila en la que desea ubicar su Fragata entre la A y la J: ")
                filafrag=filafrag.upper()
            filafrag2=nombrefilas.index(filafrag) #posicion fila
            #seleccionar columna
            while True:
                try:
                    colufrag=int(input("Seleccione la columna en la que desea ubicar su Destructor entre la 1 y la 10: "))
                    while colufrag not in nombrecolumnas:
                        colufrag=int(input("Columna inexistente. Seleccione la columna en la que desea ubicar su Destructor entre la 1 y la 10: "))
                    colufrag2=colufrag-1 #posicion columna
                    break
                except ValueError:
                    print("Ingreso un valor incorrecto. Recuerde que la columna debe ser nombrada con un numero entre el 1 y el 10.")
        
            filas = len(matriz)
            columnas = len(matriz[0])
            for f in range(filas):
                for c in range(columnas):
                    if matriz[filafrag2][colufrag2] != llenado:
                        disponible = True
            if disponible == True:
                print('Ubicacion disponible')
            else:
                print('Ubicacion no dispobile')
                
        matriz[filafrag2][colufrag2] = "X"
        print()

#funciones juego

def turno_jugador(tableroposicion,tablerojuego):
    '''Realizada los disparo para ambos jugadores usando todos los tableros disponibles'''
    nombrefilas=["A","B","C","D","E","F","G","H","I","J"]
    nombrecolumnas=[numero for numero in range(1,11)]
    disponible = False
    acerto = False
    while disponible == False:
        fila = input("Seleccione la fila para disparar entre la A y la J: ")
        fila = fila.upper()
        while fila not in nombrefilas:
            fila=input("La fila seleccionada no existe. Seleccione la fila para disparar entre la A y la J: ")
            fila=fila.upper()
        fila=nombrefilas.index(fila)
        while True: #columna
            try:
                columna=int(input("Seleccione la Columna para disparar entre la 1 y la 10: "))
                while columna not in nombrecolumnas:
                    columna=int(input("Columna inexistente. Seleccione la Columna para disparar entre la 1 y la 10: "))
                columna=columna-1 #posicion columna
                break
            except ValueError:
                print("Ingreso un valor incorrecto. Recuerde que la columna debe ser nombrada con un numero entre el 1 y el 10.")
    #fila y columna seleccionada
        if tableroposicion[fila][columna] != '#' and tableroposicion[fila][columna] != 'A': #chequeo que no haya disparado en esa posicion antes
            disponible = True
            if tablerojuego[fila][columna] == "X":
                print("Disparo acertado. Dió en el blanco.")
                disparo=True
                acerto=True
                tablerojuego[fila][columna]="#"
                tableroposicion[fila][columna]="#"
            else:
                tableroposicion[fila][columna]="A"
                print("Agua. Mejor suerte en el próximo intento.")
        else:
            print("La posición seleccionada ya fue elegida en turnos anteriores. Seleccione otra nuevamente.")
    return acerto
    

#Programa principal
print('BATALLA NAVAL'.center(80,'-'))
print()
print('Primera parte: Ubicacion de barcos de ambos jugadores')

#jugador 1
tablerojuego1=crear_tableros()
tableroposicion1=crear_tableros()
#jugadoo 2
tablerojuego2=crear_tableros()
tableroposicion2=crear_tableros()

archivo = crear_archivo()
print('Archivo disponible con las normas de juego')
print('-'*80)
print()

#carga de barcos jugador 1 
print('-Inicio ubicacion de barcos Jugador 1-'.center(80,' '))
cargar_portaaviones(tablerojuego1)
print('Portaaviones ubicado')
imprimir_tablero(tablerojuego1)
print()
cargar_submarinos(tablerojuego1)
print('Submarinos ubicados')
imprimir_tablero(tablerojuego1)
print()
cargar_destructor(tablerojuego1)
print('Destructores ubicados')
imprimir_tablero(tablerojuego1)
print()
cargar_fragata(tablerojuego1)
imprimir_tablero(tablerojuego1)
print('Fragatas ubicadas')
print()
#tablero final con barcos ubicados
print('-Carga del Jugador 1 finalizada-'.center(80,' '))
imprimir_tablero(tablerojuego1)
limpiar_pantalla()
print('_'*80) #barra separadora
#carga finalizada del usuario 1

#carga de barcos jugador 2
print('-Inicio ubicacion de barcos Jugador 2-'.center(80,' '))
cargar_portaaviones(tablerojuego2)
print('Portaaviones ubicados')
imprimir_tablero(tablerojuego2)
print()
cargar_submarinos(tablerojuego2)
print('Portaaviones cargado')
imprimir_tablero(tablerojuego2)
print()
cargar_destructor(tablerojuego2)
print('Destructores ubicados')
imprimir_tablero(tablerojuego2)
print()
cargar_fragata(tablerojuego2)
imprimir_tablero(tablerojuego2)
print('Fragatas ubicadas')
print()
#tablero final con barcos ubicados
print('-Carga del Jugador 2 finalizada-'.center(80,' '))
imprimir_tablero(tablerojuego2)
limpiar_pantalla()
#carga finalizada del usuario 2
###BARCOS CARGADOS###

###EMPIEZA LA BATALLA###
vidaJ1,vidaJ2 = 22,22
turnos = 15
disparo = False #disparo acertado 
#turnoJ1,turnoJ2 = False,False

while (vidaJ1 > 0 or vidaJ2 > 0) and turnos > 0: #mientras uno tenga vida o haya turnos
    
    print('Tablero de disparos - Turno jugador 1')
    imprimir_tablero(tableroposicion1)
    disparo=turno_jugador(tableroposicion1,tablerojuego2)
    if disparo == True: #disparo acertado
        vidaJ2 -= 1
        print("El jugador 2 ha perdido una vida. Quedando así con",vidaJ2,"vidas.")
    limpiar_pantalla_turnos()
    print('Tablero de disparos - Turno jugador 2')
    imprimir_tablero(tableroposicion2)
    disparo=turno_jugador(tableroposicion2,tablerojuego1)
    if disparo == True:
        vidaJ1 -= 1
        print("El jugador 1 ha perdido una vida. Quedando así con",vidaJ1,"vidas.")
    turnos -= 1 #termina un turno para ambos jugadores
    limpiar_pantalla_turnos()

#mensaje final por finalizacion de turnos
mayor= 0
if turnos == 0:
    limpiar_pantalla()
    print('_'*90)
    print('_'*90)
    print()
    print('Se acabaron los turnos!'.center(90,' '))
    if vidaJ1 > vidaJ2:
        mayor,menor = vidaJ1,vidaJ2
        ganador,perdedor = 'Jugador 1','Jugador 2'
    else:
        mayor,menor  = vidaJ2,vidaJ1
        ganador,perdedor = 'Jugador 2','Jugador 1'
    print()
    if ganador == 'Jugador 1':
        print('El ganador del juego es el jugador 1!!'.center(90,' '))
    else:
        print('El ganador del juego es el jugador 2!!'.center(90,' '))
    print()
    print('Felicidades capitan!!'.center(90,' '))
    print()
    print()
    print('Vidas restantes ganador:',ganador,'-',mayor,'vidas /// Segundo puesto:',perdedor,'-',menor,"vidas.")
    print('_'*90)
    print('_'*90)
    print()
    print('-Juego finalizado-')

#Uno de los dos jugadores gano
if vidaJ1 == 0 or vidaJ2 == 0:
    limpiar_pantalla()
    print('_'*90)
    print('_'*90)
    print()
    print('Se acabo el juego!'.center(90,' '))
    if vidaJ1 > vidaJ2:
        mayor,menor = vidaJ1,vidaJ2
        ganador,perdedor = 'Jugador 1','Jugador 2'
    else:
        mayor,menor  = vidaJ2,vidaJ1
        ganador,perdedor = 'Jugador 2','Jugador 1'
    print()
    if ganador == 'Jugador 1':
        print('El ganador del juego es el jugador 1!!'.center(90,' '))
    else:
        print('El ganador del juego es el jugador 2!!'.center(90,' '))
    print('Felicidades capital!! Destruiste todos los barcos del rival!'.center(80,' '))
    print()
    print()
    print('Vidas restantes ganador:',ganador,'-',mayor)
    print()
    print('_'*90)
    print('_'*90)
    print()
    print('-Juego finalizado-')
