Año=int(input("Ingrese el año de la fecha que desea consultar: "))
Mes=int(input("Ingrese el mes de la fecha que desea consultar: "))
Dia=int(input("Ingrese el día - en numero - de la fecha que desea consultar: "))
StatusAño=""
StatusMes=""
StatusDia=""
TipoDeMes=""
TipoDeAño=""
if Año>=-9999 and Año<=9999:
    StatusAño="Año valido"
else:
    StatusAño="Año invalido"
if Mes>=1 and Mes<=12:
    StatusMes="Mes valido"
else:
    StatusMes="Mes invalido"
if Mes==1 or Mes==3 or Mes==5 or Mes==7 or Mes==8 or Mes==10 or Mes==12:
    TipoDeMes="Mes de 31 días"
elif Mes==4 or Mes==6 or Mes==9 or Mes==11:
    TipoDeMes="Mes de 30 días"
elif Mes==2:
    TipoDeMes="Mes de 28 o 29 días"
else:
    TipoDeMes="Mes Invalido"
if Año%4==0 and Año%400==0:
    TipoDeAño="Año bisiesto"
elif Año%4==0 and Año%100!=0:
    TipoDeAño="Año bisiesto"
else:
    TipoDeAño="Año normal"
if (TipoDeMes=="Mes de 31 días" and (Dia>=1 and Dia<=31)) or (TipoDeMes=="Mes de 30 días" and (Dia>=1 and Dia<=30)) or (TipoDeAño=="Año bisiesto" and TipoDeMes=="Mes de 28 o 29 días" and (Dia>=1 and Dia<=29)) or (TipoDeAño=="Año normal" and TipoDeMes=="Mes de 28 o 29 días" and (Dia>=1 and Dia<=28)):#1,3,5,7,8,10,12 tienen 31 dias /4,6,9,11 tienen 30 dias/ 2 tiene 28 dias a excepción de que el año sea bisiesto
    StatusDia="Día valido"
else:
    StatusDia="Día invalido"
if StatusAño=="Año valido" and StatusMes=="Mes valido" and StatusDia=="Día valido":
    print("La fecha ingresada es valida")
   
else:
    print("La fecha ingresada es invalida")
  
    