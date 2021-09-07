# Desarrollar una función que reciba tres números enteros positivos y verifique si
# corresponden a una fecha válida (día, mes, año). Devolver True o False según la
# fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de
# la función.

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
    
def esbisiesto(x):
    if x % 4 == 0 and x % 400 == 0:
        tipo = "bisiesto" 
    elif x % 4 == 0 and x % 100 != 0:
        tipo = "bisiesto"
    else:
        tipo = "no bisiesto"
    return tipo

# Programa principal:

año=int(input("Ingrese un año: "))
tipodeaño=esbisiesto(año)
mes=int(input("Ingrese un mes: "))
dia=int(input("Ingrese un día: "))
valido=fechavalida(dia,mes,tipodeaño)
if valido == True:
    print("La fecha es valida")
else:
    print("La fecha es invalida")
    