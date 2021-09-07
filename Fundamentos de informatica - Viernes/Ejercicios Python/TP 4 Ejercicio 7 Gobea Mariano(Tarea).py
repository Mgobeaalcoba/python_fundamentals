Qpaginas=int(input("Ingrese la cantidad de hojas del libro: "))
CostoBaseRustica=125
AdicPag=2.2
CostoBaseTela=CostoBaseRustica+80
CostoBaseEspecial=CostoBaseTela+136
if Qpaginas<=300:
    print("El costo del libro es de $",CostoBaseRustica+(AdicPag*Qpaginas))
elif Qpaginas>300 and Qpaginas<=600:
    print("El costo del libro es de $",CostoBaseTela+(AdicPag*Qpaginas))
else:
    print("El costo del libro es de $",CostoBaseEspecial+(AdicPag*Qpaginas))

