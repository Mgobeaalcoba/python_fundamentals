# En los siguientes ejercicios utilice una de las funciones anteriores para ingresar datos
# en una lista y luego resuelva:

# Una escuela necesita conocer cuántos alumnos cumplen años en cada mes del año, con el
# propósito de ofrecerles un agasajo especial en su día. Desarrollar un programa que lea
# el número de legajo y fecha de nacimiento (día, mes y año) de cada uno de los alumnos
# que concurren a dicha escuela. La carga finaliza con un número de legajo igual a -1.
# Emitir un informe donde aparezca (mes por mes) cuántos alumnos cumplen años a lo largo
# del año. Mostrar también una leyenda que indique cuál es el mes con mayor cantidad de
# cumpleaños.

leg=int(input("Ingrese el numero de legajo"))   #Robado. Muy bien resuelto
mayor=0
cump=[0,0,0,0,0,0,0,0,0,0,0,0,0]
while leg != -1:
    dia=int(input("ingese dia de nacimiento"))
    mes=int(input("ingese mes de nacimiento"))
    anio=int(input("ingese año de nacimiento"))
    i=mes
    cump[i]=cump[i]+1
    if cump[i]>mayor:
        mayor=cump[i]
    leg=int(input("Ingrese el numero de legajo"))
for i in range (1,13):
    print("En el mes ", i, "hay ",cump[i],"cumpleaños")
for i in range (1,13):
    if mayor==cump[i]:
        print("El mes de mayor cumpleaños es ", i)
    