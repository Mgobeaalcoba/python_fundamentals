# Ejercicio 2
# Cargar una lista con números ingresados por un usuario hasta que se ingresa un -1
# (fin de a carga de los datos) y reemplazar un valor en una posición determinada por el
# usuario.
# Imprimir la lista antes y después del reemplazo.

# Funciones

def cargarlista():        #Cargar lista
    lista=[]
    n=int(input("Ingrese el numero que desea incorporar a la lista o -1 para terminar: "))
    while n != -1:
        lista.append(n)
        n=int(input("Ingrese el numero que desea incorporar a la lista o -1 para terminar: "))
    return lista

def imprimirlista(lista):  #Imprimir lista
    largo=len(lista)
    for i in range(largo):
        print(lista[i],end=" ")
    print()

# Programa Principal:

milista=cargarlista()
print("La lista cargada es: ")
imprimirlista(milista)
subindice=len(milista)-1
print("Ingrese el sub-índice en el que desea reemplazar un dato entre 0 y",subindice,":",end=" ")
pos=int(input())
while pos < 0 or pos > subindice:
    print("Dato ingresado invalido. Ingrese el sub-índice en el que desea reemplazar un dato entre 0 y",subindice,":",end=" ")
    pos=int(input())
print("Ingrese el nuevo dato a introducir en el subindice:",pos,":",end=" ")
dato=int(input())
milista[pos]=dato
print("La lista con el dato reemplazado es: ")
imprimirlista(milista)
