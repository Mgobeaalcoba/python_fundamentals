# Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese
# el número 999. Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de
# edad de ambos grupos. Descartar valores que no representan una edad válida. (Se considera válido una
# edad entre 0 y 100). 
 
lista = []
n = int(input("Ingrese la edad de la persona o 999 si desea terminar: "))
while n != 999 and n > 100 or n < 0:
    n = int(input("Edad ingresada invalidad. Ingrese la edad de la persona entre 0 y 100 o 999 para terminar: "))
cont1 = 0 #Mayor o igual a 18
cont2 = 0 #Menor a 18
suma1= 0
suma2= 0

while n != 999:
    lista.append(n)
    if n >= 18:
        cont1 = cont1 + 1
        suma1 = suma1 + n
    else:
        cont2 = cont2 + 1
        suma2 = suma2 + n
    n = int(input("Ingrese la edad de la persona o 999 si desea terminar: "))
    while n != 999 and n > 100 or n < 0:
        n = int(input("Edad ingresada invalidad. Ingrese la edad de la persona entre 0 y 100 o 999 para terminar: "))
        
if cont1 != 0:   
    prom1 = suma1 / cont1
    print("La cantidad de mayores o iguales a 18 años es de:",cont1,"y su promedio de edad es de:",prom1)
else:
    print("No se registraron mayores o iguales a 18 años de edad.")
if cont2 != 0:
    prom2 = suma2 / cont2
    print("La cantidad de menores de 18 años es de:",cont2,"y su promedio de edad es de:",prom2)
else:
    print("No se registraron menores de 18 años de edad.")