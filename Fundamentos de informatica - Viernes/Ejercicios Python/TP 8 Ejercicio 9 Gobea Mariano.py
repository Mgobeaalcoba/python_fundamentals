# En los siguientes ejercicios utilice una de las funciones anteriores para ingresar datos
# en una lista y luego resuelva:

# Desarrollar un algoritmo que permita ingresar 5 números pertenecientes a la lista A y
# otros 5 números pertenecientes a la lista B. Crear una lista C, donde cada posición es
# el resultado de la suma del número en la misma posición en la lista A con el número en
# la misma posición en la lista B. Ejemplo: Se ingresa A = [1, 2, 3, 4, 5] y
# B = [4, 7, 1, 3, 6] → C = [5, 9, 4, 7, 11]

def cargarlista():
    lista=[]
    for i in range(5):
        n=int(input("Ingrese un numero para ingresar a la lista: "))
        lista.append(n)
    return lista

def sumarlista(lista1,lista2):
    lista3=[]
    for i in range(5):
        lista3.append(lista1[i]+lista2[i])
    return lista3

def imprimirlista(lista):
    for i in range(len(lista)):
        print(lista[i],end=" ")
    print()

milistaA=cargarlista()
print("Lista A cargada.")
milistaB=cargarlista()
print("Lista B cargada.")
milistaC=sumarlista(milistaA,milistaB)
imprimirlista(milistaA)
imprimirlista(milistaB)
imprimirlista(milistaC)

