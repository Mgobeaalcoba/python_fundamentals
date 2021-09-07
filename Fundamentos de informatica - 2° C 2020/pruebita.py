# Hora de jugar: Desarrollar un programa que genere un número entero al azar de cuatro cifras
# y proponerle al usuario que lo descubra, ingresando valores repetidamente hasta hallarlo.
# En cada intento el programa mostrará mensajes indicando si el número ingresado es mayor o
# menor que el valor secreto. Permitir que el usuario abandone al ingresar -1. Informar la
# cantidad de intentos realizada al terminar el juego, haciendo que el usuario ingrese su número
# de documento si mejoró la mejor marca de intentos obtenida hasta el momento. Luego mostrar la
# lista ordenada de los 5 mejores puntajes (indicando también a quién pertenecen) y preguntar si
# se desea jugar otra vez, reiniciando el juego en caso afirmativo.

import random
def generarnumeroazar():
    n=random.randint(1000,9999)
    return n

def cargarlista(lista,dato):
    lista.append(dato)
    return lista

def metododeseleccion2(lista,lista2):   #Ordenamiento de arreglos relacionados
    largo=len(lista2)
    for i in range(largo-1):
        for j in range (i+1,largo):
            if lista[i] > lista[j]:
                aux = lista2[i]
                lista2[i] = lista2[j]
                lista2[j] = aux
                aux2 = lista[i]
                lista[i] = lista[j]
                lista[j] = aux2
                
def imprimirlistas(lista1,lista2): #Impresión de listas conjuntas por renglones
    largo=len(lista1)
    print("Mejores marcas:")
    for i in range(largo):
        print(lista1[i],"obtenida por:",lista2[i])

# Programa Principal

numero=5000
marcas=[]
documentos=[]


reinicio=True
while reinicio:
    reinicio=False
    
    juego=int(input("Se ha generado un número de 4 cifras. Adivine cual es o ingrese -1 si desea abandonar: "))
    while juego != -1 and (juego < 1000 or juego > 9999):
        juego=int(input("Numero ingresado invalido. Recuerde que el numero debe ser de 4 cifras o -1 para finalizar: "))

    intentos=1    
                
    while juego != numero and juego != -1:
        if juego < numero:
            juego=int(input("El número ingresado es menor al número a adivinar. Ingrese un número mayor o -1 para finalizar: "))
            while juego != -1 and (juego < 1000 or juego > 9999):
                juego=int(input("Numero ingresado invalido. Recuerde que el numero debe ser de 4 cifras o -1 para finalizar: "))
            intentos=intentos+1
        elif juego > numero:
            juego=int(input("El número ingresado es mayor al número a adivinar. Ingrese un número menor o -1 para finalizar: "))
            while juego != -1 and (juego < 1000 or juego > 9999):
                juego=int(input("Numero ingresado invalido. Recuerde que el numero debe ser de 4 cifras o -1 para finalizar: "))
            intentos=intentos+1
            
    if juego == numero:
        print("¡¡¡Felicitaciones!!! Ha ganado el juego en",intentos,"intentos.")
        if len(marcas) == 0:
            cargarlista(marcas,intentos)
            documento=int(input("Nuevo record. Introduzca su DNI: "))
            cargarlista(documentos,documento)
            metododeseleccion2(marcas,documentos)
            
        elif len(marcas) != 0 and intentos <= marcas[0]:
            cargarlista(marcas,intentos)
            documento=int(input("Nuevo record. Introduzca su DNI: "))
            cargarlista(documentos,documento)
            metododeseleccion2(marcas,documentos)
            
        imprimirlistas(marcas,documentos)
    
    else:
        print("Usted ha salido del juego. Vuelva a intentarlo mas tarde.")

    pregunta=input("¿Desea volver a jugar? si o no:")
    while pregunta != "si" and pregunta != "no":
        pregunta=input("Respuesta invalida. ¿Desea volver a jugar? si o no:")
    if pregunta == "si":
        reinicio=True

print("Adios. Lo esperamos prontó nuevamente.")
