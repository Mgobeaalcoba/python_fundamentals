# Metodo de inserción - Ordenamiento

def metododeinsercion(lista):
    for i in range(1,len(lista)): #Empieza en el segundo elemento de la lista. Propio de este metodo
        aux = lista[i]
        j = i
        while j > 0 and lista[j-1] > aux:
            lista[j] = lista[j-1]
            j = j-1
        v[j] = aux

