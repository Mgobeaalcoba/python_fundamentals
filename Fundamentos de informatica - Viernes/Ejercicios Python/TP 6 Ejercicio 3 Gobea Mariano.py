cantidad=int(input("Ingrese la cantidad de articulos que desea llevar o -1 si desea finalizar el programa: "))
while cantidad <= -2 or cantidad == 0:
    cantidad=int(input("Cantidad ingresada invalida. Ingrese la cantidad de articulos que desea llevar o -1 si desea finalizar el programa: "))
if cantidad != -1:
    preciobase=float(input("Ingrese el precio base del articulo que está vendiendo: "))

qtotal,qventasbase,ventasbase,qventas10,ventas10,qventas25,ventas25,totalventa=0,0,0,0,0,0,0,0

while cantidad != -1:
    
    qtotal=qtotal+cantidad
    
    if cantidad < 13:
        ventasbase=cantidad
        qventasbase=qventasbase+cantidad
        totalventa=(ventasbase*preciobase)+(ventas10*(preciobase-(preciobase*10/100)))+(ventas25*(preciobase-(preciobase*25/100)))
        print("El total de su venta es de: $",totalventa," y el precio promedio por unidad es de: $",totalventa/cantidad,".")
        cantidad=int(input("Ingrese la cantidad de articulos que desea llevar o -1 si desea finalizar el programa: "))
        while cantidad <= -2 or cantidad == 0:
            cantidad=int(input("Cantidad ingresada invalida. Ingrese la cantidad de articulos que desea llevar o -1 si desea finalizar el programa: "))
        if cantidad != -1:
            preciobase=float(input("Ingrese el precio base del articulo que está vendiendo: "))
    
    elif cantidad >= 13 and cantidad < 101:
        ventasbase=12
        qventasbase=qventasbase+12
        ventas10=cantidad-12
        qventas10=qventas10+(cantidad-12)
        totalventa=(ventasbase*preciobase)+(ventas10*(preciobase-(preciobase*10/100)))+(ventas25*(preciobase-(preciobase*25/100)))
        print("El total de su venta es de: $",totalventa," y el precio promedio por unidad es de: $",totalventa/cantidad,".")
        cantidad=int(input("Ingrese la cantidad de articulos que desea llevar o -1 si desea finalizar el programa: "))
        while cantidad <= -2 or cantidad == 0:
            cantidad=int(input("Cantidad ingresada invalida. Ingrese la cantidad de articulos que desea llevar o -1 si desea finalizar el programa: "))
        if cantidad != -1:
            preciobase=float(input("Ingrese el precio base del articulo que está vendiendo: "))
        
        
    else:
        ventasbase=12
        qventasbase=qventasbase+12
        ventas10=88
        qventas10=qventas10+88
        ventas25=cantidad-100
        qventas25=qventas25+(cantidad-100)
        totalventa=(ventasbase*preciobase)+(ventas10*(preciobase-(preciobase*10/100)))+(ventas25*(preciobase-(preciobase*25/100)))
        print("El total de su venta es de: $",totalventa," y el precio promedio por unidad es de: $",totalventa/cantidad,".")
        cantidad=int(input("Ingrese la cantidad de articulos que desea llevar o -1 si desea finalizar el programa: "))
        while cantidad <= -2 or cantidad == 0:
            cantidad=int(input("Cantidad ingresada invalida. Ingrese la cantidad de articulos que desea llevar o -1 si desea finalizar el programa: "))
        if cantidad != -1:
            preciobase=float(input("Ingrese el precio base del articulo que está vendiendo: "))
        
        
print("La cantidad total de ventas es de:",qtotal,".")
print("La cantidad de ventas con 10% de descuento es de:",qventas10,".")
print("La cantidad de ventas con precio base es de:",qventasbase,".")
print("La cantidad de ventas con 25% de descuento es de:",qventas25,".") # No lo pedía la consigna pero lo agregue porque me ordenaba el esquema mental.