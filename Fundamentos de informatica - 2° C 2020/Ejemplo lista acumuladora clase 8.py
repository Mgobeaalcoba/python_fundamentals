# Ejemplo listas como acumulador:
# Una empresa cuenta con 50 vendedores, numerados del 1 al 50. Por cada venta realizada se
# ingresa el numero de vendedor y el importe de la misma, donde el numero de vendedor -1
# indica el final de los datos. Estos datos no están ordenados. Realizar un programa para
# imprimir el total de ventas por vendedor.

def cargarlista(largo):
    lista=[]
    for i in range(largo):
        lista.append(0)
    return lista
    
def imprimirventas(lista):
    largo=len(lista)
    for i in range(largo):
        print("El vendedor",i+1,"realizó ventas por un total de:",lista[i])

VENDEDORES=50
milista=cargarlista(VENDEDORES)
vend=int(input("Ingrese el numero de vendedor o -1 para terminar: "))
while vend > VENDEDORES or vend < -1 or vend == 0:
    vend=int(input("Dato invalido. Ingrese el numero de vendedor nuevamente: "))
while vend != -1:
    monto=float(input("Ingrese el monto de la venta: "))
    milista[vend-1] = milista[vend-1] + monto
    vend=int(input("Ingrese el numero de vendedor o -1 para terminar: "))
    while vend > VENDEDORES or vend < -1:
        vend=int(input("Dato invalido. Ingrese el numero de vendedor nuevamente: "))

imprimirventas(milista)
