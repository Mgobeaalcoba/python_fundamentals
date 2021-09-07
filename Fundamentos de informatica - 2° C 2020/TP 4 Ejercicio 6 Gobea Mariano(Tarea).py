visitante1nombre=input("Ingrese el nombre del primer visitante: ")
visitante1edad=int(input("Ingrese la edad del primer visitante: "))
visitante1altura=float(input("Ingrese la altura del primer visitante (En mts): "))
visitante2nombre=input("Ingrese el nombre del segundo visitante: ")
visitante2edad=int(input("Ingrese la edad del segundo visitante: "))
visitante2altura=float(input("Ingrese la altura del segundo visitante (En mts): "))
if visitante1edad>=15 and visitante1altura>=1.5:
    print(visitante1nombre,"puede ingresar a la montaña rusa")
else:
    print(visitante1nombre,"no puede ingresar a la montaña rusa")
if visitante2edad>=15 and visitante2altura>=1.5:
    print(visitante2nombre,"puede ingresar a la montaña rusa")
else:
    print(visitante2nombre,"no puede ingresar a la montaña rusa")
    