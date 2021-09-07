nota=int(input("Ingrese una nota: "))
ALUMNOS=5
suma=0
a=1
while a<=ALUMNOS:
    suma=suma+nota
    a=a+1
    if a==6:
        print("El promedio de notas es de: ",suma/ALUMNOS)
    else:
        nota=int(input("Ingrese una nota: "))

    
