entero=int(input("Ingrese un numero entero positivo o cero: "))
while entero < 0:
    entero=int(input("Valor ingresado invalido. Ingrese un numero entero positivo o cero: "))
    
if entero%2 == 1:
    contador=1
else:
    contador=0

while entero > 9 or entero < -9:
    entero=entero//10
    if entero%2 == 1:
        contador += 1
       
print("El numero ingresado tiene",contador,"digitos impares.")