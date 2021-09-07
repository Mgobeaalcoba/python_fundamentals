a=int(input("Ingrese el año de una fecha: "))
m=int(input("Ingrese el mes de una fecha: "))
d=int(input("Ingrese el día de una fecha: "))
n=int(input("Ingrese la cantidad de días que desea sumar: "))

sumaraños=n//365.25
restoaños=n%365.25
sumarmeses=restoaños//30.4375
restomeses=restoaños%30.4375
sumardias=int(restomeses)

a2=a+sumaraños
m2=m+sumarmeses
d2=d+sumardias

while m2 > 12 or d2 > 31:

    tipodeaño="normal"
    if a2%4==0 and a2%400==0:
        tipodeaño="bisiesto"
    elif a2%4==0 and a2%100!=0:
        tipodeaño="bisiesto"
    
    if m2 > 12:
        a2=a2+1
        m2=m2-12
    else:
        m2=m2
    

    if (m2==1 or m2==3 or m2==5 or m2==7 or m2==8 or m2==10 or m2==12) and d2 > 31:
        m2=m2+1
        d2=d2-31
    elif (m2==1 or m2==3 or m2==5 or m2==7 or m2==8 or m2==10 or m2==12) and d2 <= 31:
        d2=d2
    elif (m2==4 or m2==6 or m2==9 or m2==11) and d2 > 30:
        m2=m2+1
        d2=d2-30
    elif (m2==4 or m2==6 or m2==9 or m2==11) and d2 <= 30:
        d2=d2
    elif m2==2 and d2 > 28 and tipodeaño=="normal":
        m2=m2+1
        d2=d2-28
    elif m2==2 and d2 <= 28 and tipodeaño=="normal":
        d2=d2
    elif m2==2 and d2 > 29 and tipodeaño=="bisiesto":
        m2=m2+1
        d2=d2-29
    elif m2==2 and d2 <= 29 and tipodeaño=="bisiesto":
        d2=d2


print("El resultado de sumar",n,"días a la fecha ingresada es:",d2,"/",int(m2),"/",int(a2),".")

