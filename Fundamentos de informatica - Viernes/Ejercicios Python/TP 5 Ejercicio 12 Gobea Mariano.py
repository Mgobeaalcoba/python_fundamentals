nombre=input("Ingrese el nombre del jugador o escriba fin si desea comparar puntajes: ")
puntos=int(input("Ingrese la cantidad de puntos obtenidos por el jugador: "))
contador=0
mayor=puntos
menor=puntos
while nombre !="fin":
    if puntos > mayor:
        mayor=puntos
        nombremayor=nombre
    if puntos <= menor:
        menor=puntos
        nombremenor=nombre
    contador=contador+1
    nombre=input("Ingrese el nombre del jugador: ")
    if nombre!="fin":
        puntos=int(input("Ingrese la cantidad de puntos obtenidos por el jugador o escriba fin si desea comparar puntajes: "))
print("El jugador con el mayor puntaje -",mayor,"- es",nombremayor,". El jugador con el menor puntaje -",menor,"- es",nombremenor,". La cantidad de jugadores entre el de mejor puntaje y el de peor puntaje es de:",contador-2,".")
    