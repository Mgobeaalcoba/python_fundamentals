# Diseñar una función que reciba dos números enteros como parámetros enteros A y B, y permita obtener AB mediante multiplicaciones sucesivas.

#función
def potenciar(a,b):
    contador = 1
    potencia = a
    while b != contador:
        potencia = potencia * a
        contador += 1
    return potencia

#Programa Principal
A=int(input("Ingrese un numero: "))
B=int(input("Ingrese otro numero: "))
resultado = potenciar(A,B)
print("El producto entre",A,"y ",B,"es de:",resultado,".")

