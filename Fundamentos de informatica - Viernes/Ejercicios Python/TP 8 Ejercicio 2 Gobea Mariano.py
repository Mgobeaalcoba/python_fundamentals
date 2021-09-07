# Escribir una función para crear una lista con N números al azar en un rango de valores que
# se recibe por parámetro. La función devuelve la lista cargada (o vacía si el rango indicado
# no es válido).
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

for i in range(tamaño):
    print(milista[i],end=" ")
print()
 