ViajeMinimo=50
kmcaro=20
kmbarato=15
Qkmviaje=float(input("¿Que cantidad de km realizó? "))
if Qkmviaje<=10:
    print("El precio del viaje realizado es de $",ViajeMinimo+(kmcaro*Qkmviaje))
else:
    print("El precio del viaje realizado es de $",ViajeMinimo+(kmbarato*Qkmviaje))
    