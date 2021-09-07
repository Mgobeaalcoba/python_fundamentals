# Escribir una función que solicite ingresar una serie de números entre 1 y 20 y guardarlos
# en una lista. En caso de ingresar un valor fuera de rango el programa mostrará un mensaje
# de error y solicitará un nuevo número. Para finalizar la carga se deberá ingresar -1. La
# función no recibe ningún parámetro, y devuelve la lista cargada (o vacía, si el usuario
# no ingresó nada) como valor de retorno.

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
        
        