entero=int(input("Ingrese un numero entero: "))
contador=1
acumulador=entero
while acumulador <=100:
    contador = contador+1
    entero=int(input("Ingrese un numero entero: "))
    if entero!=0 and entero%2==0:
        acumulador=acumulador+entero
print("Se han ingresado:",contador,"numeros")
