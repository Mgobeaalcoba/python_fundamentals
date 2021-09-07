# Devolver los últimos N dígitos de un número entero. Devolver el número completo si N es demasiado
# grande. Ejemplo: ultimosdigitos(12345,3) devuelve 345, y ultimosdigitos(12345,8) devuelve 12345.

# Funcion

def digitar(entero,digitos):
    resultado = entero % (10 ** digitos)
    return resultado

    
# Programa Principal
num=int(input("Ingrese un numero entero: "))
extrae=int(input("Ingrese la cantidad de digitos que desea extraer: "))
print("El numero a extraer es:",digitar(num,extrae))
     