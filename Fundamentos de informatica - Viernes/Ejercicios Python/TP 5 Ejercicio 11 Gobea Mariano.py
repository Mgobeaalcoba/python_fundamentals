numerovendedor=int(input("Ingrese un numero entre el 1 y 3: "))
while numerovendedor <1 or numerovendedor >3:
    numerovendedor=int(input("El numero de legajo no existe. Por favor vuelva a ingresar un numero entre 1 y 3: "))
venta=float(input("Ingrese el valor del vehiculo vendido o 0 si es fin de mes y desea cerrar su liquidación: "))
salariobase=50000
acumulador1=0
acumulador2=0
acumulador3=0
while venta !=0:
    
    if numerovendedor==1:
        comision=venta*1.5/100
        acumulador1 = acumulador1 + comision
        numerovendedor=int(input("Ingrese un numero entre el 1 y 3: "))
        while numerovendedor <1 or numerovendedor >3:
            numerovendedor=int(input("El numero de legajo no existe. Por favor vuelva a ingresar un numero entre 1 y 3: "))
        venta=float(input("Ingrese el valor del vehiculo vendido o 0 si es fin de mes y desea cerrar su liquidación."))
    elif numerovendedor==2:
        comision=venta*1.5/100
        acumulador2 = acumulador2 + comision
        numerovendedor=int(input("Ingrese un numero entre el 1 y 3: "))
        while numerovendedor <1 or numerovendedor >3:
            numerovendedor=int(input("El numero de legajo no existe. Por favor vuelva a ingresar un numero entre 1 y 3: "))
        venta=float(input("Ingrese el valor del vehiculo vendido o 0 si es fin de mes y desea cerrar su liquidación."))
    else:
        comision=venta*1.5/100
        acumulador3 = acumulador3 + comision
        numerovendedor=int(input("Ingrese un numero entre el 1 y 3: "))
        while numerovendedor <1 or numerovendedor >3:
            numerovendedor=int(input("El numero de legajo no existe. Por favor vuelva a ingresar un numero entre 1 y 3: "))
        venta=float(input("Ingrese el valor del vehiculo vendido o 0 si es fin de mes y desea cerrar su liquidación."))
        
print("El sueldo bruto del vendedor 1 es de:",salariobase+acumulador1)
print("El sueldo bruto del vendedor 2 es de:",salariobase+acumulador2)
print("El sueldo bruto del vendedor 3 es de:",salariobase+acumulador3)