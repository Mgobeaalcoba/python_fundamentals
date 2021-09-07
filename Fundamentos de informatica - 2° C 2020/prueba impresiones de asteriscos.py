#Funcion

def imprimir(titulo,asteriscos):
    contador1=1
    contador2=1
    while asteriscos != contador1:
        print("*",end="")
        contador1 += 1
    print("\n",titulo)
    while asteriscos != contador2:
        print("*",end="")
        contador2 += 1
    return
   
#Programa Principal

titulo=input("Ingrese el titulo que desea imprimir: ")
asteriscos=int(input("Ingrese la cantidad de asteriscos que desea imprimir: "))
resultado = imprimir(titulo,asteriscos)
