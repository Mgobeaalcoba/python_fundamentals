# He contado 35 cabezas y 94 patas entre las gallinas y los conejos de mi granja. ¿Cuantos conejos y cuantas gallinas tengo?.
# Verificar todas las combinaciones posibles hasta hallar la correcta. No realizar una solución algebraica. 

cabezas=35
patas=94
gallinas=1
conejos=34
patagallina=2
pataconejo=4
while gallinas*patagallina + conejos*pataconejo != patas:
    gallinas += 1
    conejos -= 1
print("La cantidad de gallinas es de: ",gallinas,". Y la cantidad de conejos es de: ",conejos,".")

