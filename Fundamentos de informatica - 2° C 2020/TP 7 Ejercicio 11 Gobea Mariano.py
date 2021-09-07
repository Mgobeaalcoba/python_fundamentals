# Diseñar una función que solicite por teclado un número y lo retorne solo si el número ingresado es
# natural, caso contrario la función deberá seguir solicitando el número por teclado. 

# Función
def comprobar(numero):
    while numero < 0:
        numero = int(input("El numero ingresado no es natural. Ingrese otro: "))
    return numero

# Programa Principal
num=int(input("Ingrese un numero: "))
print(comprobar(num))
    
    