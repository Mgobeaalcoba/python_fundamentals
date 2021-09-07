legajo=int(input("Ingrese el numero de legajo o -1 para terminar: "))
if legajo != -1:
    nota=int(input("Ingrese la nota obtenida - entre 1 y 10 - : "))
    while nota <1 or nota >10:
        nota=int(input("Ingreso un valor invalido. Ingrese la nota obtenida - entre 1 y 10 - : "))
aprobados=0
desaprobados=0
aplazados=0
totalalumnos=0

while legajo!= -1:
    
    totalalumnos += 1
    
    if nota >= 4:
        print("El estudiante con legajo número:",legajo,"aprobó el examen final.")
        aprobados += 1
        legajo=int(input("Ingrese el numero de legajo o -1 para terminar: "))
        if legajo != -1:
            nota=int(input("Ingrese la nota obtenida - entre 1 y 10 - : "))
            while nota <1 or nota >10:
                nota=int(input("Ingreso un valor invalido. Ingrese la nota obtenida - entre 1 y 10 - : "))
    elif nota < 4 and nota != 1:
        print("El estudiante con legajo número:",legajo,"desaprobó el examen final.")
        desaprobados += 1
        legajo=int(input("Ingrese el numero de legajo o -1 para terminar: "))
        if legajo != -1:
            nota=int(input("Ingrese la nota obtenida - entre 1 y 10 - : "))
            while nota <1 or nota >10:
                nota=int(input("Ingreso un valor invalido. Ingrese la nota obtenida - entre 1 y 10 - : "))
    else: # nota == 1
        print("El estudiante con legajo número:",legajo,"desaprobó el examen final y está aplazado.")
        desaprobados += 1
        aplazados += 1
        legajo=int(input("Ingrese el numero de legajo o -1 para terminar: "))
        if legajo != -1:
            nota=int(input("Ingrese la nota obtenida - entre 1 y 10 - : "))
            while nota <1 or nota >10:
                nota=int(input("Ingreso un valor invalido. Ingrese la nota obtenida - entre 1 y 10 - : "))
            
if aprobados == 0:
    print("No hubo estudiantes aprobados")
elif aprobados == 1:
    print("Aprobo el examen final 1 solo estudiante")
else:
    print("Aprobaron el examen final",aprobados,"estudiantes.")
    
if desaprobados == 0:
    print("No hubo estudiantes desaprobados")
elif desaprobados ==1:
    print("Desaprobó el examen final 1 solo estudiante")
else:
    print("Desaprobaron el examen final",desaprobados,"estudiantes.")
    
if aplazados == 0:
    print("No hubo estudiantes aplazados")
else:
    print("El porcentaje de estudiantes aplazados es del:",(aplazados*100)/totalalumnos,"%.")

    
        
    