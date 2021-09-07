salariobase=50000
venta=float(input("Ingrese el valor del vehiculo vendido o 0 si es fin de mes y desea cerrar su liquidación: "))
acumuladorventas=0
contadorventas=0

while venta !=0:
    comision=venta*1.5/100
    acumulador = acumulador + comision
    contadorventas=contadorventas+1
    venta=float(input("Ingrese el valor del vehiculo vendido o 0 si es fin de mes y desea cerrar su liquidación: "))
    
print("El sueldo bruto del vendedor es de:",salariobase+acumulador)