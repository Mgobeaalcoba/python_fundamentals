#Función

def obtener_mes_en_texto(numero_mes):
    if numero_mes < 1 or numero_mes > 12:
        mestexto = "Valor ingresado invalido. Ingrese un numero del 1 al 12."
    elif numero_mes == 1:
        mestexto = "Enero"
    elif numero_mes == 2:
        mestexto = "Febrero"
    elif numero_mes == 3:
        mestexto = "Marzo"
    elif numero_mes == 4:
        mestexto = "Abril"
    elif numero_mes == 5:
        mestexto = "Mayo"
    elif numero_mes == 6:
        mestexto = "Junio"
    elif numero_mes == 7:
        mestexto = "Julio"
    elif numero_mes == 8:
        mestexto = "Agosto"
    elif numero_mes == 9:
        mestexto = "Septiembre"
    elif numero_mes == 10:
        mestexto = "Octubre"
    elif numero_mes == 11:
        mestexto = "Noviembre"
    else:
        mestexto = "Diciembre"
    return mestexto

#Programa Principal

mes=int(input("Ingrese el numero de mes que desea pasar a texto - entre 1 y 12 - : "))
print(obtener_mes_en_texto(mes))


    