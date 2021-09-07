#Función

def comparar(a,b):
    if a > b:
        print("El máximo introducido es:", a)
    else:
        print("El máximo introducido es:", b)
    return

#Programa Principal

x=float(input("Ingrese un numero: "))
y=float(input("Ingrese otro numero: "))
esmayor = comparar(x,y)
