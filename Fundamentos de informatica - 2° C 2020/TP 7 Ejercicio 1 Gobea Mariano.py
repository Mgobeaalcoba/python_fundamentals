#Función que reciba dos parametros numéricos enteros, calcule y devuelva el resultado de la
# multiplicación de ambos utilizando solo sumas

#función
def multiplicar(a,b):
    contador = 1
    producto = a
    while b != contador:
        producto = producto + a
        contador += 1
    return producto

#Programa Principal
x=int(input("Ingrese un numero: "))
y=int(input("Ingrese otro numero: "))
resultado = multiplicar(x,y)
print("El producto entre",x,"y ",y,"es de:",resultado,".")

