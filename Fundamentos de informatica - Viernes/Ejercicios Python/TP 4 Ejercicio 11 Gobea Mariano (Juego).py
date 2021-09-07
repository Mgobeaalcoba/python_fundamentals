Año=int(input("Ingrese un año: "))
if Año%4==0 and Año%400==0:
    print("El año ingresado es bisiesto")
elif Año%4==0 and Año%100!=0:
    print("El año ingresado es bisiesto")
else:
    print("El año ingresado no es bisiesto")
