precio=float(input("Ingrese el precio actual del producto X o -1 para terminar: "))
while precio < -1 or precio == 0:
    precio=float(input("El precio no puede ser negativo o cero. Ingrese el precio actual del producto X o -1 para terminar: "))

contador=0
acumulador2000=0
contador2000=0
acumulador3000a5000=0
contador3000a5000=0
mayor=precio
menor=precio

while precio != -1:
    
    contador += 1
    
    if precio < 2000:
        contador2000 += 1
        acumulador2000 = acumulador2000+precio
    
    if precio >= 3000 and precio <= 5000:
        contador3000a5000 += 1
        acumulador3000a5000 = acumulador3000a5000+precio
        
    if precio > mayor:
        mayor = precio
        
    if precio < menor:
        menor = precio
        
    precio=float(input("Ingrese el precio actual del producto X o -1 para terminar: "))
    
print("La cantidad total de precios informados para el producto X es de:",contador)
if contador2000 != 0:
    print("El promedio de los precios menores a 2000 pesos ingresados es de:",acumulador2000/contador2000)
else:
    print("El producto X no ha tenido ningún precio menor a 2000. Por lo que no es posible informar el promedio entre ellos.")
if contador3000a5000 != 0:
    print("La cantidad de precios entre 3000 y 5000 pesos ingresados es de:",contador3000a5000)
else:
    print("El producto X no ha tenido ningún precio mayor a 3000 y menor a 5000.")
if mayor == -1 or menor == -1:
    print("Usted no ha ingresado ningún precio. Por lo que no es posible definir cual es el mayor y el menor.")
else:
    print("El precio mas caro ingresado es de:",mayor,". Y el mas barato es de:",menor,".")

    
        
