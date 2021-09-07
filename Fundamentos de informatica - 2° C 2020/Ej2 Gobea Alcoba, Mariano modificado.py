entero=int(input("Ingrese un numero entero positivo o cero: "))
while entero < 0:
    entero=int(input("Valor ingresado invalido. Ingrese un numero entero positivo o cero: "))
contador=0

while entero > 0:
    
    if entero%2 == 1:
        contador += 1
        
    entero=entero//10
       
print("El numero ingresado tiene",contador,"digitos impares.")