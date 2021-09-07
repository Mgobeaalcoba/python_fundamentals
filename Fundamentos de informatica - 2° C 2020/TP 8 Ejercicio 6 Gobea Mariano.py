# En los siguientes ejercicios utilice una de las funciones anteriores para ingresar datos
# en una lista y luego resuelva:

# Determinar si una lista es capicúa. La lista puede tener cualquier tipo de dato básico
# que vimos en clase.

def cargarlista():
    lista = []
    n=int(input("Ingrese un numero entre 1 y 20 o -1 para finalizar la carga: "))
    while n == 0 or n < -1:
        n=int(input("Numero ingresado invalido. Ingrese un numero entre 1 y 20 o -1 para finalizar la carga: "))
    while n != -1:
        lista.append(n)
        n=int(input("Ingrese un numero entre 1 y 20 o -1 para finalizar la carga: "))
        while n == 0 or n < -1:
            n=int(input("Numero ingresado invalido. Ingrese un numero entre 1 y 20 o -1 para finalizar la carga: "))
    return lista

milista = cargarlista()
largo = len(milista)

i=0
j=largo-1
capicua=False
while milista[i] == milista[j] and i < j:
    i = i + 1
    j = j - 1
if i >= j:
    capicua=True
    print("La lista ingresada es capicua.")
else:
    capicua=False
    print("La lista ingresada NO es capicua.")

    
