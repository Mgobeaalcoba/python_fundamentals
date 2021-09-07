# Metodo de intercambio o burbujeo - Clase 8

def metododeintercambio(lista): # Metodo de ordenamiento numero 2.
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range (len(lista)-1):
            if lista[i] > lista[i+1]:
                aux = lista [i]
                lista[i] = lista [i+1]
                lista[i+1] = aux
                desordenado = True



