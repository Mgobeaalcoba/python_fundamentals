SueldoBasico=float(input("Ingrese su sueldo básico: "))
Antiguedad=int(input("Ingrese sus años de antiguedad: "))
EstadoCivil=input("Ingrese su estado civil con \"c\" si es casado o \"s\" si es soltero: ")
AntiguedadAplicada=""
if EstadoCivil=="c":
    AntiguedadAplicada=Antiguedad*(SueldoBasico*7/100)
else:
    AntiguedadAplicada=Antiguedad*(SueldoBasico*5/100)
SueldoConformado=SueldoBasico+AntiguedadAplicada
Jubilación=(SueldoConformado*11/100)
ObraSocial=(SueldoConformado*3/100)
Sindicato=(SueldoConformado*3/100)
if EstadoCivil=="c":
    print("Estado Civil: Casado/a")
    print("Sueldo básico        Antiguedad     Descuentos     Importe")
    print("$   ",SueldoBasico,"                ",Antiguedad,"                 +",SueldoBasico+AntiguedadAplicada)
    print("                                    Jubilación   ","-",Jubilación)
    print("                                    Obra Social  ","-",ObraSocial)
    print("                                    Sindicato    ","-",Sindicato)
    print("                     Sueldo Neto                 ","$",SueldoConformado-Jubilación-ObraSocial-Sindicato)
else:    
    print("Estado Civil: Soltero/a")
    print("Sueldo básico        Antiguedad     Descuentos     Importe")
    print("$   ",SueldoBasico,"                ",Antiguedad,"                 +",SueldoBasico+AntiguedadAplicada)
    print("                                    Jubilación   ","-",Jubilación)
    print("                                    Obra Social  ","-",ObraSocial)
    print("                                    Sindicato    ","-",Sindicato)
    print("                     Sueldo Neto                 ","$",SueldoConformado-Jubilación-ObraSocial-Sindicato)
input() # Hace que el programa no termine hasta apretar Enter
