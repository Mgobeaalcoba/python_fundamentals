nombre=input("Ingrese el nombre del alumno o presione enter para finalizar: ")
if nombre != "":
    notapractica=int(input("Ingrese la nota - entre 1 y 10 - obtenida en prácticas: "))
    while notapractica < 1 or notapractica > 10:
        notapractica=int(input("Valor ingresado invalido. Ingrese la nota - entre 1 y 10 - obtenida en prácticas: "))
    notaproblemas=int(input("Ingrese la nota - entre 1 y 10 - obtenida en problemas: "))
    while notaproblemas < 1 or notaproblemas > 10:
        notaproblemas=int(input("Valor ingresado invalido. Ingrese la nota - entre 1 y 10 - obtenida en problemas: "))
    notateorica=int(input("Ingrese la nota - entre 1 y 10 - obtenida en teóricos: "))
    while notateorica < 1 or notateorica > 10:
        notateorica=int(input("Valor ingresado invalido. Ingrese la nota - entre 1 y 10 - obtenida en teóricos: "))
else:
    print("Usted no ha ingresado ningún nombre.")
    
while nombre != "":
    print("El alumno",nombre,"obtuvo como nota final un:",(notapractica*10/100)+(notaproblemas*50/100)+(notateorica*40/100))
    
    nombre=input("Ingrese el nombre del alumno o presione enter para finalizar: ")
    if nombre != "":
        notapractica=int(input("Ingrese la nota - entre 1 y 10 - obtenida en prácticas: "))
        while notapractica < 1 or notapractica > 10:
            notapractica=int(input("Valor ingresado invalido. Ingrese la nota - entre 1 y 10 - obtenida en prácticas: "))
        notaproblemas=int(input("Ingrese la nota - entre 1 y 10 - obtenida en problemas: "))
        while notaproblemas < 1 or notaproblemas > 10:
            notaproblemas=int(input("Valor ingresado invalido. Ingrese la nota - entre 1 y 10 - obtenida en problemas: "))
        notateorica=int(input("Ingrese la nota - entre 1 y 10 - obtenida en teóricos: "))
        while notateorica < 1 or notateorica > 10:
            notateorica=int(input("Valor ingresado invalido. Ingrese la nota - entre 1 y 10 - obtenida en teóricos: "))
            
print("Fin del programa. Muchas gracias por habernos elegido.")
    
    