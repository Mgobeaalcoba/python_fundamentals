# Dadas los siguientes arreglos apareados nombres y edades, se pide ordenar por edad
# de menor a mayor (recuerde que, entre arreglos relacionados, las posiciones
# indican la relación que hay entre los datos de estos, así en el ejemplo, el nombre
# “Juan” se corresponde con la edad 28, “Pablo” con la edad 22, etc.):
# nombres = [‘Juan’, ‘Pablo’, ‘Damián’, ‘Manuel’, ‘Nahuel’, ‘Lucas’]
# edades = [ 28, 22, 12, 18, 25, 43 ]

# Funciones

def metododeseleccion(lista,lista2):   #Ordenamiento de arreglos relacionados
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
                
def imprimirlista(lista):
    for i in range(len(lista)):
        print(lista[i],end=" ")
    print()

# Programa Principal

nombres = ["Juan", "Pablo", "Damián", "Manuel", "Nahuel", "Lucas"]
edades = [ 28, 22, 12, 18, 25, 43 ]

imprimirlista(nombres)
imprimirlista(edades)

print("Ordenamos listas de menor a mayor en función de las edades.")

metododeseleccion(nombres,edades)
imprimirlista(nombres)
imprimirlista(edades)



