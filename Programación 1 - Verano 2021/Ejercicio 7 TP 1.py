# Escribir una función diasiguiente(…) que reciba como parámetro una fecha cualquiera expresada por tres enteros
# (correspondientes al día, mes y año) y calcule y devuelva tres enteros correspondientes al
# día siguiente al dado.
# Utilizando esta función, desarrollar programas que permitan:
# a. Sumar N días a una fecha.
# b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.

# Funciones:

def esbisiesto(x):
    if x % 4 == 0 and x % 400 == 0:
        tipo = "bisiesto" 
    elif x % 4 == 0 and x % 100 != 0:
        tipo = "bisiesto"
    else:
        tipo = "no bisiesto"
    return tipo

def fechavalida(x,y,tipo):
    fecha=True
    if y > 12 or y < 1:
        fecha=False
    if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12:
        if x > 31 or x < 1:
            fecha=False
    elif tipo == "bisiesto" and y == 2:
        if x > 29 or x < 1:
            fecha=False
    elif tipo == "no bisiesto" and y == 2:
        if x > 28 or x < 1:
            fecha=False
    else:
        if x > 30 or x < 1:
            fecha=False
    return fecha

def diasiguiente(d,m,a,tipo):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d == 31 and m == 12:
            a += 1
            m = 1
            d = 1
        elif d == 31 and m != 12:
            m += 1
            d = 1
        else:
            d += 1
    elif tipo == "bisiesto" and m == 2:
        if d == 29:
            m += 1
            d = 1
        else:
            d += 1
    elif tipo == "no bisiesto" and m == 2:
        if d == 28:
            m += 1
            d = 1
        else:
            d += 1
    else:
        if d == 30:
            m += 1
            d = 1
        else:
            d += 1
    return d,m,a,tipo

# Programa principal:

valido=False
while valido == False:
    año=int(input("Ingrese un año: "))
    tipodeaño=esbisiesto(año)
    mes=int(input("Ingrese un mes: "))
    dia=int(input("Ingrese un día: "))
    valido=fechavalida(dia,mes,tipodeaño)
    if valido == False:
        print("Fecha invalida. Intente nuevamente.")
    
sumardias=int(input("¿Cuantos días desea sumar? "))
for i in range (sumardias):
    dia ,mes , año , tipodeaño = diasiguiente(dia,mes,año,tipodeaño)
    tipodeaño=esbisiesto(año)

print("La fecha con los días sumados es: ",dia,"/",mes,"/",año,sep="")

# Segundo programa:

print("El siguiente programa le permitirá calcular la cantidad de días existentes entre dos días cualquiera.")

print("A continuación se le solicitará el año, mes y día de la primera fecha.")

valido=False
while valido == False:
    año2=int(input("Ingrese un año: "))
    tipodeaño2=esbisiesto(año2)
    mes2=int(input("Ingrese un mes: "))
    dia2=int(input("Ingrese un día: "))
    valido=fechavalida(dia,mes,tipodeaño)
    if valido == False:
        print("Fecha invalida. Intente nuevamente.")
        
print("Ahora se le pedirá que ingrese la segunda fecha sobre la cual desea calcular la cantidad de días.")

valido=False
while valido == False:
    año3=int(input("Ingrese un año: "))
    tipodeaño23=esbisiesto(año3)
    mes3=int(input("Ingrese un mes: "))
    dia3=int(input("Ingrese un día: "))
    valido=fechavalida(dia,mes,tipodeaño)
    if valido == False:
        print("Fecha invalida. Intente nuevamente.")
    
cont = 0
while año3 != año2 or mes3 != mes2 or dia3 != dia2:
    dia2 ,mes2 , año2 , tipodeaño2 = diasiguiente(dia2,mes2,año2,tipodeaño2)
    tipodeaño2=esbisiesto(año2)
    cont += 1

print("La cantidad de días entre la primera fecha ingresada y la segunda es de:",cont)
    