# Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y un entero N,
# y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original. Escribir también un
# programa para verificar el comportamiento de la misma.
# Hacer tres versiones de la función, para cada uno de los siguientes casos:
# a.Utilizando sólo ciclos normales
# b.Utilizando listas por comprensión
# c.Utilizando la función filter

def filtrar_palabras(string,N):
    cont=0
    nueva=" "
    newstring=""
    for i in range(len(string)):
        if string[i] != " " and string[i] != "." and string[i] != ",":
            cont += 1
            if i == len(string)-1:
                if cont >= N:
                    newstring=newstring+string[i-cont+1:i+1]
        else:
            if cont >= N:
                newstring=newstring+string[i-cont:i]+nueva
            cont = 0
    return newstring

def filtrar_palabras2(string,N):
    stringlist=string.split()   # El split se aplica inicializando una lista antes de usarla
    stringlist2=list(filter(lambda x: len(x) >= N , stringlist))   #El filter crea una lista nueva filtrando otra existente
    stringlist3=' '.join(stringlist2)
    return stringlist3

def filtrar_palabras3(string,N):
    lista=string.split()
    lista2=[i for i in lista if len(i) >= N]
    cadena=' '.join(lista2)
    return cadena
    
# Programa principal:
cadena=input("Ingrese una frase: ")
print(cadena)
print(len(cadena))
n=int(input("Ingrese un numero entero mediante el cual desee filtrar la frase: "))
print(n)
filtrada=filtrar_palabras3(cadena,n)
print(filtrada)


    
