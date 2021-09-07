zona=int(input("Ingrese el numero de zona o -1 para terminar: "))
while zona < -1 or zona >2 or zona ==0:
    zona=int(input("Valor ingresado invalido. Ingrese el numero de zona o -1 para terminar: "))

if zona != -1:

    if zona == 1:
        zona=CABA
    elif zona == 2:
        zona=GBA
    sexo=int(input("Ingrese 1 si es hombre y 2 si es mujer."))
    while zona < 1 or zona > 2:
        sexo=int(input("Valor ingresado invalido. Ingrese 1 si es hombre y 2 si es mujer."))
    if sexo == 1:
        sexo=hombre
    else:
        sexo=mujer
    menu=int(input("Ingrese el numero de menu - entre 1 y 3 - seleccionado: "))
    while menu < 1 or menu > 3:
        menu=int(input("Valor ingresado invalido. Ingrese el numero de menu - entre 1 y 3 - seleccionado: "))
    if menu == 1:
        menu=250
    elif menu == 2:
        menu=400
    else:
        menu=500

else:
    print("Fin del programa")



    