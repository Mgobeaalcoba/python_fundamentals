# La siguiente función permite averiguar el día de la semana para una fecha determinada. La fecha se suministra en forma de tres
# parámetros enteros y la función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para imprimir
# por pantalla el calendario de un mes completo, correspondiente a un mes y año cualquiera basándose en la función suministrada.
# Considerar que la semana comienza en domingo.

#Funciones: 

def diadelasemana(dia,mes,año):
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def diasdelmes (y,tipo):
    if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12:
        mes = 31
    elif tipo == "bisiesto" and y == 2:
        mes = 29
    elif tipo == "no bisiesto" and y == 2:
        mes = 28
    else:
        mes = 30
    return mes

def esbisiesto(x):
    if x % 4 == 0 and x % 400 == 0:
        tipo = "bisiesto" 
    elif x % 4 == 0 and x % 100 != 0:
        tipo = "bisiesto"
    else:
        tipo = "no bisiesto"
    return tipo

#Programa principal: 

listatitulo = ["D ","L ","M ","X ","J ","V ","S "]
milista = []
mes=int(input("Ingrese el numero de mes que desea imprimir su calendario: "))
año=int(input("Ingrese el numero de año al que pertenece el mes que deses imprimir: "))
print()
tipodeaño=esbisiesto(año)
diasmes=diasdelmes(mes,tipodeaño)
dia=1
diasemana=diadelasemana(dia,mes,año)

#Cargar lista
for i in range (diasemana):
    milista.append(0)
for i in range (1,diasmes+1):
    milista.append(i)

#Imprimir Lista
for i in range (len(listatitulo)):
    print(listatitulo[i],end=" ")
print()
for i in range (len(milista)):
    if milista[i] == 0:
        print("  ",end=" ")
    else:
        if i % 7 != 0:
            print("%02d" %milista[i],end=" ")
        else:
            print()
            print("%02d" %milista[i],end=" ")
 