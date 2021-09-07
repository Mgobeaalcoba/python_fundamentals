# He contado 35 cabezas y 94 patas entre las gallinas y los conejos de mi granja. ¿Cuantos conejos y cuantas gallinas tengo?.
# Verificar todas las combinaciones posibles hasta hallar la correcta. No realizar una solución algebraica. 

cabezas=35
patas=94
gallinas=int(input("¿Cuantas gallinas cree que hay? - Recuerde: Contó 35 cabezas y 94 patas: ")) 
while gallinas > cabezas:
    gallinas=int(input("No le alcanzan las cabezas. Pruebe otra vez. ¿Cuantas gallinas cree que hay?: "))
cabezas -= gallinas
patas -= (gallinas*2)
if patas % 4 != 0:
    print("Le quedan", patas,"patas. Y cada conejo tiene 4 patas por lo que no son multiplos. Vuelva a intentarlo nuevamente")
else:
    conejos = patas / 4
    if conejos > cabezas:
        print("Me quedan:",cabezas,"cabezas. y",patas,"patas.")
        print("No le alcanzan las cabezas. Vuelva a intentarlo nuevamente")
    elif conejos < cabezas:
        print("Me quedan:",cabezas,"cabezas. y",patas,"patas.")
        print("Le sobran cabezas. Vuelva a intentarlo nuevamente.")
    else:
        print("Perfecto. La cantidad de gallinas es de: ", gallinas, "y la cantidad de conejos es de: ", conejos)
