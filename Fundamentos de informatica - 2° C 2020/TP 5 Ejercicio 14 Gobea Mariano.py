a=int(input("Ingrese un numero entero positivo: "))
while a <0:
    a=int(input("Ingreso un numero negativo. Ingrese por favor un numero entero positivo: "))
b=int(input("Ingrese otro numero entero positivo: "))
while b <0:
    b=int(input("Ingreso un numero negativo. Ingrese por favor otro numero entero positivo: "))
contador=0
acumulador=0
while contador != b:
    acumulador=acumulador + a
    contador= contador + 1
print("El producto de la operación es:",acumulador,".")

    
