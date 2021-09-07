legajo=int(input("Ingrese el numero de legajo o -1 para terminar: "))
if legajo!= -1:
    categoria=input("Ingrese la categoria del empleado \(A, B o C\): ")
    while categoria != "A" and categoria != "B" and categoria != "C":
        categoria=input("Dato invalido. Ingrese la categoria del empleado \(A, B o C\): ")
    salario=float(input("Ingrese el salario del empleado: "))
    mayorsalario=salario
    menorsalario=salario
    legajomayorsalario=legajo
    legajomenorsalario=legajo
    empleados=0
    totalsalarios=0
    totala=0
    totalb=0
    totalc=0
    empleados20000=0
    empleados5000yc=0
    
while legajo != -1:
    
    totalsalarios=totalsalarios+salario
    empleados=empleados+1
    
    if salario > mayorsalario:
        mayorsalario=salario
        legajomayorsalario=legajo
    elif salario < menorsalario:
        menorsalario=salario
        legajomenorsalario=legajo
        
    if categoria == "A":
        totala=totala+salario
    elif categoria == "B":
        totalb=totalb+salario
    elif categoria == "C":
        totalc=totalc+salario
        if salario < 5000:
            empleados5000yc=empleados5000yc+1
    
    if salario > 20000:
        empleados20000=empleados20000+1
        
    legajo=int(input("Ingrese el numero de legajo o -1 para terminar: "))
    if legajo!= -1:
        categoria=input("Ingrese la categoria del empleado \(A, B o C\): ")
        while categoria != "A" and categoria != "B" and categoria != "C":
            categoria=input("Dato invalido. Ingrese la categoria del empleado \(A, B o C\): ")
        salario=float(input("Ingrese el salario del empleado: "))
if empleados == 0:
    print("No ha ingresado información de ningun empleado aún.")
else:
    print("El importe total de salarios pagados por la empresa es de: $",totalsalarios,".")
    print("La cantidad de empleados que ganan mas de $20000 es de:",empleados20000,".")
    print("La cantidad de empleados que ganas menos de $5000 y son de categoria C es de:",empleados5000yc,".")
    print("El legajo del empleado que mas gana es el:",legajomayorsalario,".")
    print("El sueldo mas bajo es de: $",menorsalario,".")
    print("El total de sueldos devengados a empleados de categoria A es de: $",totala,". El de categoria B es de: $",totalb,". El de categoria C es de: $",totalc,".")
    print("El sueldo promedio de la empresa es de: $",totalsalarios/empleados,".")
    
    

