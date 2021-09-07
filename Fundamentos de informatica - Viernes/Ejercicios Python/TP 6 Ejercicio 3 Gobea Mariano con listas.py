# Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
# • Aplica el precio base a la primera docena de unidades.
# • Aplica un 10% de descuento a todas las unidades entre 13 y 100.
# • Aplica un 25% de descuento a todas las unidades por encima de las 100.
# Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100.
# El cálculo resultante sería: 
 
# 100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04 
 
# Escribir un algoritmo que lea la cantidad solicitada de un producto y su precio base,
# y muestre el valor total de la venta y el precio promedio por unidad. El fin de carga se
# determina ingresando -1 como cantidad solicitada.  Al finalizar informar:
# a) Cantidad de ventas realizadas total.
# b) Cantidad de ventas que se aplicaron un 10% de descuento.
# c) Cantidad de ventas que SOLO se aplicó el precio base, no se le realizaron descuentos.

unidadesbase = []
unidades10 = []
unidades25 = []
unidadestotales =[]

n=int(input("Ingrese la cantidad de productos vendidos o -1 para terminar: "))
while n < -1 or n == 0:
    n=int(input("Numero ingresado invalido. Ingrese un numero positivo o -1 para terminar: "))
if n != -1:
    p=float(input("Ingrese su precio: "))

while n != -1:
    if n > 12 and n < 101:
        unidadesbase.append(12)
        unidades10.append(n-12)
        unidadestotales.append(n)
        n=int(input("Ingrese la cantidad de productos vendidos o -1 para terminar: "))
        while n < -1 or n == 0:
            n=int(input("Numero ingresado invalido. Ingrese un numero positivo o -1 para terminar: "))
        if n != -1:
            p=float(input("Ingrese su precio: "))
    elif n >= 101:
        unidadesbase.append(12)
        unidades10.append(88)
        unidades25.append(n-100)
        unidadestotales.append(n)
        n=int(input("Ingrese la cantidad de productos vendidos o -1 para terminar: "))
        while n < -1 or n == 0:
            n=int(input("Numero ingresado invalido. Ingrese un numero positivo o -1 para terminar: "))
        if n != -1:
            p=float(input("Ingrese su precio: "))
    else:
        unidadesbase.append(n)
        unidadestotales.append(n)
        n=int(input("Ingrese la cantidad de productos vendidos o -1 para terminar: "))
        while n < -1 or n == 0:
            n=int(input("Numero ingresado invalido. Ingrese un numero positivo o -1 para terminar: "))
        if n != -1:
            p=float(input("Ingrese su precio: "))

suma = 0
contar = 0
suma10 = 0
contar10 = 0
suma25 = 0
contar25 = 0
sumatotal = 0
contartotal = 0

i = 0
for i in range(len(unidadesbase)):
    suma = suma + unidadesbase[i]
    contar = contar + 1
i = 0
for i in range(len(unidades10)):
    suma10 = suma10 + unidades10[i]
    contar10 = contar10 + 1
i = 0  
for i in range(len(unidades25)):
    suma25 = suma25 + unidades25[i]
    contar25 = contar25 + 1
i = 0
for i in range(len(unidadestotales)):
    sumatotal = sumatotal + unidadestotales[i]
    contartotal = contartotal + 1
    

print("La cantidad de ventas totales realizadas es de:",sumatotal)
print("La cantidad de ventas a las que se aplico el 10% de descuento es de:",suma10)
print("La cantidad de ventas a las que solo se le aplicó el precio base es de:",suma)

