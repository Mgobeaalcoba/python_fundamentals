# Escribir una función espandigital(n) que determine si un numero n es pandigital, retornando True o False segun
# corresponda. Escribir también un programa para ingresar un número, invocar a la función y mostrar un mensaje
# informativo. pandigital = numero que contiene del 0 al 9 al menos una vez.

# Función:

def espandigital(n):
    """ Función que determina si el numero
    ingresado por el usuario es pandigital
    o no lo es. """
    referencia=[0,1,2,3,4,5,6,7,8,9]
    ultimo=n%10
    resto=n//10
    pandigital=False
    if n >= 1000000000:
        for i in range(len(referencia)):
            while resto > 0:
                if referencia[i] == ultimo:
                    pandigital=True
                    break
                else:
                    ultimo=resto%10
                    resto=resto//10
            if pandigital==False:
                break
    return pandigital

# Programa principal:

numero=int(input("Ingrese el número entero que desea verificar si es pandigital: "))
verificado=espandigital(numero)
if verificado == True:
    print("El número",numero,"es pandigital. Ya que contiene en si mismo todos los digitos entre 0 y 9.")
else:
    print("El número",numero,"NO es pandigital. Ya que no contiene en si mismo todos los dígitos entre 0 y 9.")
