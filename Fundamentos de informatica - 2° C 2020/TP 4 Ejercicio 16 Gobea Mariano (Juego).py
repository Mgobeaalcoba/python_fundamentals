AceroPaseo=1.5
AceroMontaña=2
PrecioPaseo=16000
PrecioMontaña=18000
StockAcero=80
QBiciPaseo=int(input("Ingrese la cantidad de bicis de paseo que desea fabricar: "))
QBiciMontaña=int(input("Ingrese la cantidad de bicis de montaña que desea fabricar: "))
if QBiciPaseo<0 or QBiciMontaña<0:
    print("Una de las cantidades de bicicletas a producir no es valida. Ingrese solamente numeros positivos.")
else:
    if StockAcero<(QBiciPaseo*AceroPaseo+QBiciMontaña*AceroMontaña):
        print("No dispone del acero suficiente en stock. Debé comprar:",(QBiciPaseo*AceroPaseo+QBiciMontaña*AceroMontaña)-StockAcero,"Kg de acero para terminar su producción.")
    else:
        print("El stock de acero es suficiente para producir las bicicletas ingresadas.")
input()
