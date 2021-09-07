# Funciones:

def escapicua(lista):
    largo=(len(lista))
    capicua=True
    i = 0
    j = -1
    while capicua == True and i < largo:
        if lista[i] != lista[j]:
            capicua=False
        else:
            i += 1
            j -= 1
    return capicua

# Programa principal:

milista=[5,4,3,2,1,2,3,4,5]
milista2=[5,4,3,2,1,1,2,3,4,5]
milista3=[4,5,1,5,7,9,0,4]

capi=escapicua(milista)
print(milista)
if capi == True:
    print("La lista es capicua")
else:
    print("La lista no es capicua")
    
capi=escapicua(milista2)
print(milista2)
if capi == True:
    print("La lista es capicua")
else:
    print("La lista no es capicua")
    
capi=escapicua(milista3)
print(milista3)
if capi == True:
    print("La lista es capicua")
else:
    print("La lista no es capicua")