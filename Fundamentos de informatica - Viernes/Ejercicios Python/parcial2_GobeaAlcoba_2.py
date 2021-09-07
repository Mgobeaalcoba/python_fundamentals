# Grabar en formato py con el nombre parcial2_apellido 
# Una empresa de taxis debe renovar los vehículos de su flota que  hayan superado un millón de kilómetros recorridos.
# Para eso necesita un programa que le permita llevar el control de dicha renovación. El programa debe realizar las siguientes
# tareas:
# 1- Ingresar el número interno de cada una de las unidades y el kilometraje recorrido por ese vehículo, finalizando la lectura
# con un número de unidad igual a -1. Controlar que el número de unidad se encuentre entre 500 y 2999, emitiendo un mensaje de
# error en caso de estar fuera de rango.
# 2- Finalizada la lectura se solicita imprimir un listado con todos los datos de las unidades que deben ser renovadas
# (unidad de renovación y kilometraje recorrido). Este listado deberá ordenarse por kilometraje recorrido, comenzando desde
# la unidad con más kilometraje. Junto a cada renglón del listado se añadirá el mensaje "BAJA POR KILOMETRAJE".
# 3- Por último se solicita informar cuántos vehículos posee la empresa, qué porcentaje de éstos debe ser renovado y el
# vehículo con menor kilometraje en poder de la misma.

# Funciones:

def metododeseleccion2(lista,lista2):            #Ordenamiento de listas de forma conjunta
    largo=len(lista2)
    for i in range(largo-1):
        for j in range (i+1,largo):
            if lista2[i] < lista2[j]:
                aux = lista2[i]
                lista2[i] = lista2[j]
                lista2[j] = aux
                aux2 = lista[i]
                lista[i] = lista[j]
                lista[j] = aux2
                
def imprimirlistas(lista1,lista2):                #Impresión condicionada
    largo=len(lista2)
    print("Unidades que deben ser renovadas:")
    for i in range(largo):
        if lista2[i] > 1000000:
            print("Unidad de renovación:",lista1[i]," Kilometraje recorrido:",lista2[i],"BAJA POR KILOMETRAJE")

# Primera parte:

taxis=[]
kilometros=[]
n=int(input("Ingrese el numero interno del taxi, entre 500 y 2999, o -1 para terminar: "))
while (n < 500 and n != -1) or n > 2999:
    n=int(input("Numero interno invalido. Intente nuevamente y recuerde que debe estar entre 500 y 2999 o ingrese -1 para finalizar: "))
while n != -1:
    taxis.append(n)
    km=int(input("Ingrese el numero de kilometros recorridos por ese vehiculo: "))
    while km < 0:
        km=int(input("Dato invalido. Ingrese el numero de kilometros recorridos por ese vehiculo: "))
    kilometros.append(km)
    n=int(input("Ingrese el numero interno del taxi, entre 500 y 2999, o -1 para terminar: "))
    while (n < 500 and n != -1) or n > 2999:
        n=int(input("Numero interno invalido. Intente nuevamente y recuerde que debe estar entre 500 y 2999 o ingrese -1 para finalizar: "))
print()

# Segunda parte:

if len(taxis) >= 1:
    metododeseleccion2(taxis,kilometros)
    imprimirlistas(taxis,kilometros)
    print()

# Tercera parte:

    renovar=0
    for i in range(len(kilometros)):
        if kilometros[i] > 1000000:
            renovar += 1
    flota=len(taxis)
    menorkm=taxis[len(taxis)-1]                # Ya está ordenado de forma descendente.
    porcentaje=renovar*100/flota

    print("La empresa posee",flota,"vehiculos")
    print("El",porcentaje,"% de los vehiculos debe ser renovado.")
    print("El vehiculo con menor kilometraje de la empresa es el interno:",menorkm)
    
else:
    print("No se ha ingresado ninguna unidad al sistema.")
    