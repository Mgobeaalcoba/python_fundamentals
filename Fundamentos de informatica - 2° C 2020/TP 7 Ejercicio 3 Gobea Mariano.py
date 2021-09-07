#Funcion

def imprimir(asteriscos):
    contador=1
    while asteriscos != contador:
        print("*",end="")
        contador += 1
    return
   
#Programa Principal

titulo=input("Ingrese el titulo que desea imprimir: ")
asteriscos=int(input("Ingrese la cantidad de asteriscos que desea imprimir: "))
resultado = imprimir(asteriscos)
print("\n",titulo)
resultado = imprimir(asteriscos)


