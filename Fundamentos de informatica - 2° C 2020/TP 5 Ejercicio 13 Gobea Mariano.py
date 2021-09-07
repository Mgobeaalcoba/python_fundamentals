ultimapatente=int(input("Ingrese el ultimo digito de la patente \(entre 0 y 9\) o -1 si desea terminar: "))
while ultimapatente < -1 or ultimapatente >9:
    ultimapatente=int(input("Ingrese un número que no está permitido. Ingrese el ultimo digito de la patente \(entre 0 y 9\) o -1 si desea terminar: "))
contadorpar=0
contadorimpar=0
while ultimapatente !=-1:
    if ultimapatente%2==0:
        contadorpar=contadorpar+1
    else:
        contadorimpar=contadorimpar+1
    ultimapatente=int(input("Ingrese el ultimo digito de la patente \(entre 0 y 9\) o -1 si desea terminar: "))
    while ultimapatente < -1 or ultimapatente >9:
        ultimapatente=int(input("Ingrese un número que no está permitido. Ingrese el ultimo digito de la patente \(entre 0 y 9\) o -1 si desea terminar: "))
print("Circularon en el día:",contadorpar,"autos con patente par y",contadorimpar,"autos con patente impar.")