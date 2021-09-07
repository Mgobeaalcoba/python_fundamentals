legajo=int(input("Ingrese el número de legajo o -1 si desea finalizar: "))
if legajo != -1:
    nota=int(input("Ingrese la nota obtenida \(entre 1 y 10\) en el examen final: "))
    while nota < 1 or nota > 10:
        nota=int(input("La nota ingresada no es valida. Ingrese la nota obtenida \(entre 1 y 10\) en el examen final: "))
contadoraprobo=0
contadordesaprobo=0
contadoraplazo=0
contadortotal=0
notamasalta=0
lejajonotaalta=0

while legajo != -1:
    contadortotal += 1
    
    if nota > notamasalta:
        notamasalta=nota
        legajonotaalta=legajo
    
    if nota >= 7:
        contadoraprobo += 1
    elif nota <= 6 and nota >= 4:
        contadordesaprobo += 1
    else:
        contadoraplazo += 1
    
    legajo=int(input("Ingrese el número de legajo o -1 si desea finalizar: "))
    if legajo != -1:
        nota=int(input("Ingrese la nota obtenida \(entre 1 y 10\) en el examen final: "))
        while nota < 1 or nota > 10:
            nota=int(input("La nota ingresada no es valida. Ingrese la nota obtenida \(entre 1 y 10\) en el examen final: "))

if contadortotal != 0:         
    print("La cantidad de alumnos con nota mayor o igual a 7 es de:",contadoraprobo,".")
    print("La cantidad de alumnos con nota entre 4 y 6 es de:",contadordesaprobo,".")
    print("El porcentaje de alumnos aplazados es de:",contadoraplazo*100/contadortotal,"%.")
    print("El total de alumnos evaluados es de:",contadortotal,".")
    print("La nota mas alta obtenida es de:",notamasalta,". Y fue obtenida por el legajo:",legajonotaalta,".")

else:
    print("No ha ingresado legajo ni nota alguna. Vuelva a intentarlo.")

