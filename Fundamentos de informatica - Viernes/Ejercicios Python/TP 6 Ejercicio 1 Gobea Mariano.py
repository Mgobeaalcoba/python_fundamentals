edad=int(input("Ingrese su edad \(entre 0 y 100\) o 999 si desea terminar: "))
if edad != 999:
    while edad <0 or edad >100:
        edad=int(input("Edad invalida. Ingrese su edad \(entre 0 y 100\) o 999 si desea terminar: "))
contadormenores=0
contadormayores=0
sumamenores=0
sumamayores=0

while edad != 999:
    if edad < 18:
        contadormenores += 1
        sumamenores += edad
        edad=int(input("Ingrese su edad \(entre 0 y 100\) o 999 si desea terminar: "))
        if edad != 999:
            while edad <0 or edad >100:
                edad=int(input("Edad invalida. Ingrese su edad \(entre 0 y 100\) o 999 si desea terminar: "))            
        
    else: # >= 18:
        contadormayores += 1
        sumamayores += edad
        edad=int(input("Ingrese su edad \(entre 0 y 100\) o 999 si desea terminar: "))
        if edad != 999:
            while edad <0 or edad >100:
                edad=int(input("Edad invalida. Ingrese su edad \(entre 0 y 100\) o 999 si desea terminar: "))
                
if contadormenores==0 and contadormayores!=0:
    print("No ha ingresado menores de 18 años. Y ha ingresado",contadormayores," mayores o iguales de 18 años cuyo promedio de edad es de: ",sumamayores/contadormayores,".")
elif contadormayores==0 and contadormenores!=0:
    print("No ha ingresado mayores de 18 años. Y ha ingresado",contadormenores," menores de 18 años cuyo promedio de edad es de: ",sumamenores/contadormenores,".")
elif contadormayores==0 and contadormenores==0:
    print("No ha ingresado ninguna edad valida. Vuelva a intentarlo")
else:
    print("Ha ingresado",contadormenores,"menores de 18 años cuyo promedio de edad es de:",sumamenores/contadormenores,". Y ha ingresado",contadormayores," mayores o iguales de 18 años cuyo promedio de edad es de: ",sumamayores/contadormayores,".")
        





