# Leer los números de legajo de los alumnos de un curso y su nota de examen final. Cargar el
# número de legajo en la lista LEGAJOS y la nota en la lista NOTA_FINAL. El fin de la carga
# se determina ingresando un -1 como legajo. Se debe validar que la nota ingresada sea entre
# 1 y 10. Terminada la carga de datos, recorrer las listas e informar: ▪ Cantidad de alumnos
# que aprobaron con nota mayor o igual a 4 ▪ Cantidad de alumnos que desaprobaron el examen.
# Nota menor a 4 ▪ Promedio de nota y los legajos que superan el promedio

def cargarlista(lista,dato):
    lista.append(dato)
    return lista
               
#Programa Principal

LEGAJOS=[]
NOTA_FINAL=[]

legajo=int(input("Ingrese el numero de legajo o -1 si desea terminar la carga: "))
while legajo != -1:
    nota=int(input("Ingrese la nota obtenida por el estudiante: "))
    while nota < 1 or nota > 10:
        nota=int(input("Valor invalido. Ingrese la nota obtenida por el estudiante, entre 1 y 10: "))
    cargarlista(LEGAJOS,legajo)
    cargarlista(NOTA_FINAL,nota)
    legajo=int(input("Ingrese el numero de legajo o -1 si desea terminar la carga: "))
    
acum=0
apro=0
desa=0

for i in range(len(NOTA_FINAL)):
    acum=acum+NOTA_FINAL[i]
    prom=acum/len(NOTA_FINAL)
    if NOTA_FINAL[i] >= 4:
        apro += 1
    else:
        desa += 1

SUPERANPROMEDIO=[]
        
for i in range(len(NOTA_FINAL)):
    if NOTA_FINAL[i] > prom:
        SUPERANPROMEDIO.append(LEGAJOS[i])
    
print("La cantidad de alumnos que aprobaron el examen es de:",apro,".")
print("La cantidad de alumnos que desaprobaron el examen es de:",desa,".")
print("El promedio de nota es de:",prom,".")
print("Los legajos por ensima del promedio son:")
for i in range(len(SUPERANPROMEDIO)):
    print(SUPERANPROMEDIO[i],end=" ")

        




