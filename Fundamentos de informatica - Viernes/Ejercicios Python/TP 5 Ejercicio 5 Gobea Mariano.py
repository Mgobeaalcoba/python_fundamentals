numeroentero=int(input("Ingrese un numero entero: "))
CANT=10
a=1
mayor=numeroentero
while a<=CANT:
    if numeroentero>mayor:
        mayor=numeroentero
        ordendeingreso=a
    a=a+1
    numeroentero=int(input("ingrese un nuevo numero entero: "))
print("El mayor de los numero es:",mayor,"y se ingreso en el orden numero:",ordendeingreso)

    