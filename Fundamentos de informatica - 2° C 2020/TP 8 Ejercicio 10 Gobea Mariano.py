# En los siguientes ejercicios utilice una de las funciones anteriores para ingresar datos
# en una lista y luego resuelva:

# Escribir una función para devolver la posición que ocupa un valor pasado como parámetro,
# utilizando búsqueda secuencial en una lista desordenada. La función debe devolver -1 si
# el elemento no se encuentra en la lista.
import random
def cargarlista():
    lista=[]
    largo=int(input("Establezca el largo de su lista: "))
    minimo=int(input("Establezca el minimo valor posible para su lista: "))
    maximo=int(input("Establezca el maximo valor posible para su lista: "))
    for i in range(largo):
        lista.append(random.randint(minimo,maximo))
    return lista

def busquedasecuencial(lista,buscado):
    largo=len(lista)
    i = 0
    posicion = -1
    while i < largo and buscado != lista[i]:
        i = i + 1
    if i < largo:
        posicion = i
    else:
        posicion = -1
    return posicion

def imprimirlista(lista):
    for i in range(len(lista)):
        print(lista[i],end=" ")
    print()

#Programa principal

milista=cargarlista()
busqueda=int(input("Ingrese el valor que desea buscar en la lista: "))
encontrado=busquedasecuencial(milista,busqueda)
imprimirlista(milista)
if encontrado == -1:
    print("El numero buscado no se encuentra en la lista.")
else:
    print("El numero buscado se encuentra en el subindice:",encontrado,".")


        