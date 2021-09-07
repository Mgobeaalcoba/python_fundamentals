numero=int(input("Ingrese un numero mayor que cero: "))
while numero <= 0:
    numero=int(input("Numero ingresado invalido. Vuelva a ingresar un numero mayor que cero: "))
multiplicador=numero-1
resultado=numero

while multiplicador != 0:
    resultado = resultado * multiplicador
    multiplicador = multiplicador - 1
    
print("El factorial de",numero,"es:",resultado,".")

