# Escribir un algoritmo que permita ingresar los números de legajo de los alumnos de un curso y su nota
# de examen final. El fin de la carga se determina ingresando un -1 en el legajo. Informar para cada
# alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. Se debe validar
# que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar: • Cantidad de alumnos
# que aprobaron con nota mayor o igual a 4. • Cantidad de alumnos que desaprobaron el examen con nota menor
# a 4. • Porcentaje de alumnos que están aplazados (tienen 1 en el examen).
  

legajos = []
notas = []
aprobados = 0
desaprobados = 0
aplazados = 0
totales = 0
leg=int(input("Ingrese un numero de legajo o -1 para finalizar: "))
if leg != -1:
    nota=int(input("Ingrese la nota sacada por dicho legajo: "))
    while nota < 1 or nota > 10:
        nota=int(input("Nota invalida. Ingrese una nota de 1 a 10: "))
    if nota >= 4:
        print ("El alumno aprobó el examen.")
        aprobados += 1
    elif nota < 4 and nota > 1:
        print ("El alumno desaprobó el examen.")
        desaprobados += 1
    else:
        print ("El alumno tiene un aplazo.")
        aplazados += 1
    totales += 1
        

while leg != -1:
    legajos.append(leg)
    notas.append(nota)
    leg=int(input("Ingrese un numero de legajo o -1 para finalizar: "))
    if leg != -1:
        nota=int(input("Ingrese la nota sacada por dicho legajo: "))
        while nota < 1 or nota > 10:
            nota=int(input("Nota invalida. Ingrese una nota de 1 a 10: "))
        if nota >= 4:
            print ("El alumno aprobó el examen.")
            aprobados += 1
        elif nota < 4 and nota > 1:
            print ("El alumno desaprobó el examen.")
            desaprobados += 1
        else:
            print ("El alumno tiene un aplazo.")
            aplazados += 1
        totales += 1
        
print("La cantidad de alumnos que aprobaron el examen es de: ",aprobados)
print("La cantidad de alumnos que desaprobaron el examen es de: ",desaprobados)
if aplazados != 0:
    print("El porcentaje de alumnos aplazados es de: ",aplazados*100/totales)
else:
    print("No se registraron aplazados en el examen.")
    
        


