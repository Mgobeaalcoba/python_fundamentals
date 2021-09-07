# Crear una lista de N números generados al azar entre 0 y 100 pero sin elementos repetidos.
# Validar que N sea menor o igual a 100.
import random

def cargarlista():  #Cargar lista sin elementos repetidos
    lista=[]
    n=random.randint(0,100)
    for i in range(n):
        lista.append(random.randint(0,100))
    for i in range(len(lista)-1):
        j=i+1
        while j < len(lista):
            if lista[i] == lista[j]:
                del lista[j]
            j=j+1
    return lista
            
def imprimirlista(lista):
    for i in range(len(lista)):
        print(lista[i],end=" ")
    print()
    
milista=cargarlista()
imprimirlista(milista)