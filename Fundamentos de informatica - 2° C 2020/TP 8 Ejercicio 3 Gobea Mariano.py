# En los siguientes ejercicios utilice una de las funciones anteriores para ingresar datos
# en una lista y luego resuelva: 
 
# Ejercicio 3: Calcular la suma de los números de una lista. 
import random
def cargarlista(largo):
    lista = []
    n1=int(input("Ingrese el minimo del rango: "))
    n2=int(input("Ingrese el maximo del rango: "))
    for i in range(largo):
        lista.append(random.randint(n1,n2))
    return lista

tamaño=int(input("Seleccione el largo de la lista: "))
milista=cargarlista(tamaño)
suma= 0

for i in range(tamaño):
    suma = suma + milista[i]
    
print("La suma de los numeros de la lista es: ",suma)