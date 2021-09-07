# Los números de claves de dos cajas fuertes están intercalados dentro de un número entero llamado "clave maestra",
# cuya longitud no se conoce. Realizar un programa para obtener ambas claves, donde la primera se construye con los
# dígitos ubicados en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en posiciones
# pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave maestra fuera 18293, la clave 1 sería 123 y
# la clave 2 sería 89.

clavemaestra=str(46923406)
clave1=""
clave2=""
for i in range(len(clavemaestra)): # Si lo recorro con for i in clavemaestra voy a recorrer cada valor del string clavemaestra(14968972) uno por uno
    if i%2 == 0:   #Si el subindice es par
        clave1 = clave1 + clavemaestra[i]
    else:                        #Si el subindice es impar
        clave2 = clave2 + clavemaestra[i]
print(clave1)
print(clave2)


