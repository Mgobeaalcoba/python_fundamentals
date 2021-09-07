# Una fábrica de bicicletas desea realizar un control de inventario de sus productos, la empresa fabrica N
# productos diferentes y quiere mantener en stock un mínimo de 5 unidades por producto. 

# Necesita un programa
# que ingrese código del producto positivo y simule la cantidad en stock actual (valor entre 1 y 50). Si se
# vuelve a ingresar un código de producto, se debe rechazar. La carga de datos finaliza con un código de
# producto igual a -1.

import random

def cargarlistasjuntas(lista1,lista2,dato1):
    dato2=random.randint(1,50)
    lista1.append(dato1)
    lista2.append(dato2)
    
def metododeseleccion2(lista,lista2):   #Ordenamiento de arreglos relacionados
    largo=len(lista2)
    for i in range(largo-1):
        for j in range (i+1,largo):
            if lista2[i] > lista2[j]:
                aux = lista2[i]
                lista2[i] = lista2[j]
                lista2[j] = aux
                aux2 = lista[i]
                lista[i] = lista[j]
                lista[j] = aux2
    
def busquedasecuencial(lista,buscado):   #Busqueda
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

def imprimirlista(lista1,lista2):
    largo=len(lista1)
    print("Código    Cantidad")
    for i in range(largo):
        print(lista1[i],"        ",lista2[i],)
    print()
    
productos=[]
stocks=[]
recompra=[]
faltan=[]

MINIMO=15

producto=int(input("Ingrese el codigo del producto que desea cargar o -1 si desea finalizar: "))
while producto != -1:
    repetido=busquedasecuencial(productos,producto)
    
    if repetido == -1:
        cargarlistasjuntas(productos,stocks,producto)
        producto=int(input("Ingrese el codigo del producto que desea cargar o -1 si desea finalizar: "))
        
    else:
        producto=int(input("Dato ingresado repetido. Ingrese el codigo del producto que desea cargar o -1 si desea finalizar: "))

# Luego de la carga, informar:
# ✓ Código del producto y cantidad en stock actual. Ordenado por Código de producto de menor a mayor. Con el
# siguiente formato:
# Código  Cantidad
#    123        20
#    243        10
#    450         3
#   8080        15

metododeseleccion2(stocks,productos)
imprimirlista(productos,stocks)

# ✓ Código del producto y cantidad en stock actual de los productos que están por debajo del stock mínimo.
# A continuación, indicar cuál es el total general de unidades faltantes para que todos los productos tengan
# al menos las 5 unidades en stock. 

unid=0
for i in range(len(productos)):
    if stocks[i] < MINIMO:
        recompra.append(productos[i])
        faltan.append(stocks[i])
        unid=unid+MINIMO-stocks[i]
        
print("Los productos con cantidades por debajo del stock mínimo son: ")
imprimirlista(recompra,faltan)
print("Para que todos los productos tengan al menos el stock minimo de",MINIMO,"unidades falta comprar:",unid,"unidades totales.")
print()
    
# ✓ Mayor cantidad en stock y todos los códigos de productos que tienen
# la mayor cantidad en stock. 

mayor=stocks[0]

for i in range(len(stocks)):
    if stocks[i] > mayor:
        mayor = stocks[i]
        
print("La mayor cantidad en stock es de: ",mayor,".")
print("Los productos con la mayor cantidad en stock son: ")
print("Código    Cantidad")
for i in range(len(productos)):
    if stocks[i] == mayor:
        print(productos[i],"        ",stocks[i],)
        
# Realizar la búsqueda de códigos de producto ingresados por teclado e informar su cantidad en stock con una
# leyenda si está por debajo del stock mínimo. Finalizar el ingreso de códigos para la búsqueda con -1.
# Informar cuántos productos de los buscados fueron encontrados.

estan=0
noestan=0
buscado=int(input("Ingrese el codigo de producto que desea consultar el stock o ingrese -1 si desea finalizar: "))
while buscado != -1:
    encontrado=busquedasecuencial(productos,buscado)
    if encontrado == -1:
        noestan += 1
        print("No se encontró el producto solicitado.")
        buscado=int(input("Ingrese el codigo de producto que desea consultar el stock o ingrese -1 si desea finalizar: "))
    else:
        estan += 1
        print("El producto buscado está en stock y tiene",stocks[encontrado],"unidades en stock")
        if stocks[encontrado] < MINIMO:
            print("El stock de este producto está por debajo del stock mínimo o de seguridad.")
        buscado=int(input("Ingrese el codigo de producto que desea consultar el stock o ingrese -1 si desea finalizar: "))

print("La cantidad de productos consultados y encontrados fue de:",estan,".")
print("La cantidad de productos consultados y no encontrados fue de:",noestan,".")
        
        
    
        
               
