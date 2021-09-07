PeriodoEnSegundos=int(input("Ingrese un periodo de tiempo en segundos: "))
PeriodoEnDias=int(PeriodoEnSegundos/86400)
RestoADias=float(PeriodoEnSegundos%86400)
PeriodoEnHoras=int(RestoADias/3600)
RestoAHoras=float(RestoADias%3600)
PeriodoEnMinutos=int(RestoAHoras/60)
RestoAMinutos=float(RestoAHoras%60)
print(PeriodoEnSegundos,"equivale a",PeriodoEnDias,"días",PeriodoEnHoras,"horas",PeriodoEnMinutos,"minutos y",int(RestoAMinutos),"segundo.")

