nombre=input("Ingrese su nombre o -1 para finalizar la jornada: ")
contador=1
primercliente=contador
ultimocliente="x"
while nombre != "-1":
    if primercliente==contador:
        primercliente=nombre
    if ultimocliente!="-1":
        ultimocliente=nombre
    contador= contador+1
    nombre=input("Ingrese su nombre o -1 para finalizar la jornada: ")
print("El primer cliente fue:",primercliente,"y el ultimo cliente fue:",ultimocliente)
