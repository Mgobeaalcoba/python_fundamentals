n=int(input("Ingrese un numero entero positivo: "))
while n <0:
    n=int(input("Ingreso un numero negativo. Ingrese por favor un numero entero positivo: "))

acumulador=0

if n%2 == 0:
    n=n-1
    while n >= 0:
        print(n)
        acumulador=acumulador+n
        n=n-2
            
else:
    while n >= 0:
        print(n)
        acumulador=acumulador+n
        n=n-2
        
print("La suma de los numeros impares mostrados es:",acumulador,".")
