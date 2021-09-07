nota1=int(input("Ingrese la nota del primer parcial: "))
nota2=int(input("Ingrese la nota del segundo parcial: "))
if nota1>=7 and nota2>=7:
    print("Promocionó la materia")
elif nota1>=4 and nota2>=4:
    print("Aprobó la materia. Debe rendir final")
else:
    print("Debe recuperar para llegar a final")
    
    