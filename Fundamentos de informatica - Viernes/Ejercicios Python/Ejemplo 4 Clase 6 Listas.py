# Primera Parte: Lectura de numeros e ingreso a la lista

lista = []
cont = 0
n=int(input("Ingrese un numero a la lista o -1 para terminar: "))
while n != -1:
    lista.append(n)
    cont = cont + 1
    n=int(input("Ingrese un numero a la lista o -1 para terminar: "))

# Segunda Parte: Identifico e imprimo el mayor y la lista entera
i = 0
pos = 0
mayor = lista [i]
for i in range (len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]
        pos = i
    i = i + 1
print("El numero mayor es:",mayor,"y está en la posición:",pos)

i = 0
for i in range (len(lista)):
    print (lista[i], end=" ")
    i = i + 1

# Tercera Parte: Elimino el mayor e imprimo la lista nuevamente

print("Borrando el mayor:",mayor)
del lista[pos]

i = 0
for i in range (len(lista)):
    print (lista[i], end=" ")
    i = i + 1
    


