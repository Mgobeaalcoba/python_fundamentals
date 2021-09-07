entero=int(input("Ingrese un numero entero: "))
contador=1

while entero > 9 or entero < -9:
    contador += 1
    entero=entero//10

print("El numero ingresado tiene:",contador,"digitos.")
    