# En los siguientes ejercicios utilice una de las funciones anteriores para ingresar datos
# en una lista y luego resuelva:

# Llenar una lista con números enteros (números positivos o negativos). Mostrar la cantidad
# de números positivos y la cantidad de números negativos que hay en dicha lista.

import random
def cargarlista(largo):
    lista = []
    n1=int(input("Ingrese el minimo del rango: "))
    n2=int(input("Ingrese el maximo del rango: "))
    for i in range(largo):
        lista.append(random.randint(n1,n2))
    return lista

# Programa principal

tamaño=int(input("Seleccione el largo de la lista: "))
milista=cargarlista(tamaño)
positivos=0
negativos=0

for i in range(tamaño):
    if milista[i] >= 0:
        positivos += 1
    else:
        negativos += 1

print("En la lista hay:",positivos,"numeros positivos y",negativos,"numeros negativos.")