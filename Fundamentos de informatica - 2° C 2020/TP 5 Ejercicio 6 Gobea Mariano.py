entero=int(input("Ingrese un numero entero o el numero 0 si desea terminar: "))
contador=0
acumulador=0
maximo=entero
minimo=entero
while entero!=0:
    acumulador=acumulador+entero
    contador=contador+1
    if entero>maximo:
        maximo=entero
    if entero<minimo:
        minimo=entero
    entero=int(input("Ingrese un numero entero o el numero 0 si desea terminar: "))
if contador==0:
    print("Usted no ha ingresado ningún número distinto de 0. Por favor vuelva a iniciar.")
else:
    promedio=acumulador/contador
    print("El máximo ingresado es:",maximo,".El minimo ingresado es:",minimo,".El promedio ingresado es:",promedio,".")
    