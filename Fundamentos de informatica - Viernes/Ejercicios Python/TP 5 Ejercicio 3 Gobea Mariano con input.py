TABLA=int(input("Ingrese el numero de la tabla que desea consultar: "))
contador=1
resultado=TABLA*contador
while contador<11:
    print(TABLA,"x",contador,"=",resultado)
    contador+=1
    resultado=TABLA*contador

