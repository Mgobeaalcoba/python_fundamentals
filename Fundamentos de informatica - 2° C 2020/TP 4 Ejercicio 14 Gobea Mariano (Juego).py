X=int(input("Ingrese el año del cual desea calcular la fecha de pascuas: "))
A=X%19
B=X%4
C=X%7
D=((A*19)+24)%30
E=((B*2)+(C*4)+(D*6)+5)%7
CodFecha=D+E+22
if CodFecha<=31:
    print("La fecha de pascuas es:",CodFecha,"de Marzo de",X)
else:
    print("La fecha de pascuas es:",CodFecha-31,"de Abril de",X)
    
input()
    