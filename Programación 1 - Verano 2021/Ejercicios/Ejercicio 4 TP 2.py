# Eliminar de una lista de palabras las palabras que se encuentren en una segunda lista. Imprimir la lista original, la lista
# de palabras a eliminar y la lista resultante.

#Funciones:

def eliminarlista (l1,l2):
    i = 0
    while i < len(l2):
        if l2[i] in l1:
            l1.remove(l2[i])
        else:
            i += 1
                   
#Programa principal:

lista1 = ["perro","gato","loro","mono","chancho","jirafa","rinoceronte","chancho","avestruz","elefante","loro"]
lista2 = ["loro","chancho","avestruz","pajaro"]

print(lista1)
print(lista2)

eliminarlista(lista1,lista2)

print(lista1)
