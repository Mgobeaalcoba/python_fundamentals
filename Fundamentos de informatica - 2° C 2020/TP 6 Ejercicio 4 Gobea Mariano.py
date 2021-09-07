cliente=int(input("Ingrese el numero de cliente: "))
factura=float(input("Ingrese el monto total de su factura: "))
descuento2=factura*2/100
recargo10=factura*10/100

print("las opciones de pago para el cliente: ",cliente,"son:")
if descuento2>120:
    print("Pagando en los primeros 10 días del mes el monto a abonar es de: $",factura-descuento2,".")
else:
    print("Pagando en los primeros 10 días del mes el monto a abonar es de: $",factura-120,".")
print("Pagando entre el día 11 y 20, el monto a abonar es de: $",factura,".")
if recargo10>150:
    print("Pagando del día 21 en adelante, el monto a abonar es de: $",factura+recargo10,".")
else:
    print("Pagando del día 21 en adelante, el monto a abonar es de: $",factura+150,".")
