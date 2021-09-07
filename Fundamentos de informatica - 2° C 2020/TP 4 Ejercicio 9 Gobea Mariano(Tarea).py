LargoAmb=float(input("Ingrese el largo del cuarto en cms: "))
AnchoAmb=float(input("Ingrese el ancho del cuarto en cms: "))
AltoAmb=float(input("Ingrese el alto del cuarto en cms: "))
AltoPuerta=float(input("Ingrese el alto de la puerta en cms: "))
AnchoPuerta=float(input("Ingrese el ancho de la puerta en cms: "))
AltoVentana=float(input("Ingrese el alto de la ventana en cms: "))
AnchoVentana=float(input("Ingrese el ancho de la ventana en cms: "))
LargoCeramica=float(input("Ingrese el largo de la ceramica a colocar en cms: "))
AnchoCeramica=float(input("Ingrese el ancho de la ceramica a colocar en cms: "))
CostoPaqueteCeramica=float(input("Ingrese el costo del paquete de ceramicas: "))
QCeramicasXPaquete=int(input("Ingrese la cantidad de ceramicas que vienen en el paquete: "))
Cms2ParedAncha=AnchoAmb*AltoAmb
Cms2ParedLarga=LargoAmb*AltoAmb
Cms2Puerta=AltoPuerta*AnchoPuerta
Cms2Ventana=AltoVentana*AnchoVentana
Cms2HabitaciónNeto=(Cms2ParedAncha*2)+(Cms2ParedLarga*2)-Cms2Puerta-Cms2Ventana
Cms2Ceramica=LargoCeramica*AnchoCeramica
QCeramicasEnCuarto=Cms2HabitaciónNeto/Cms2Ceramica
QPaquetesAComprar=QCeramicasEnCuarto/QCeramicasXPaquete
CostoCeramicas=QPaquetesAComprar*CostoPaqueteCeramica
print("Se necesitaran",QCeramicasEnCuarto,"ceramicas para construir el ambiente especificado")
print("El gasto total en ceramicas es de:",CostoCeramicas)




