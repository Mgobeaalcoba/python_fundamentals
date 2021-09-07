# Desarrollar una función que extraiga una subcadena de una cadena de caracteres, indicando la posición y la
# cantidad de caracteres deseada. Devolver la subcadena como valor de retorno. Escribir también un programa para
# verificar el comportamiento de la misma. Ejemplo, dada la cadena "El número de teléfono es 43567890" extraer la
# subcadena que comienza en la posición 25 y tiene 9 caracteres, resultando la subcadena "4356-7890". Escribir una
# función para cada uno de los siguientes casos:
# a.Utilizando rebanadas
# b.Sin utilizar rebanadas

def extraer_subcadena(cadena):
    print("La cadena de caracteres cuenta con",len(cadena),"posiciones. Entre 1 y",len(cadena),end=" ")
    posinicial=int(input("Selecciones el numero de posicion en el que desea arrancar la extracción: "))-1
    cant=int(input("Ingrese la cantidad de caracteres que desea extraer: "))
    subcadena=cadena[posinicial:posinicial+cant]
    return subcadena

def extraer_subcadena2(cadena):
    print("La cadena de caracteres cuenta con",len(cadena),"posiciones. Entre 1 y",len(cadena),end=" ")
    posinicial=int(input("Selecciones el numero de posicion en el que desea arrancar la extracción: "))-1
    cant=int(input("Ingrese la cantidad de caracteres que desea extraer: "))
    tope=posinicial+cant
    subcadena=""
    while posinicial < tope:
        subcadena = subcadena + cadena[posinicial]
        posinicial += 1
    return subcadena
        
# Programa principal:
string=input("Ingrese una cadena de texto: ")
print(string,"\n")
substring=extraer_subcadena2(string)
print(substring)
