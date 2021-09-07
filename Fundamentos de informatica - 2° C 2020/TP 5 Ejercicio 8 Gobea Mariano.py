venta=float(input("Ingrese el importe de la venta realizada o ingrese -1 cuando finaliza el día: "))
while venta <-1:
    venta=float(input("Ingreso un numero negativo. Ingrese el importe de la venta realizada o ingrese -1 cuando finaliza el día: "))
total=0
cantidad=0
while venta !=-1:
    total= total+venta
    cantidad= cantidad+1
    venta=float(input("Ingrese el importe de la venta realizada o ingrese -1 cuando finaliza el día: "))
    while venta <-1:
        venta=float(input("Ingreso un numero negativo. Ingrese el importe de la venta realizada o ingrese -1 cuando finaliza el día: "))
print("El monto total vendido fue de: $",total,". Realizó",cantidad,"de ventas en el día")
