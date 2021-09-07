# Escribir un programa para crear una lista por comprensión con los naipes de la baraja española. La lista debe
# contener cadenas de caracteres. Ejemplo: ["1 Oros", "2 Oros"... ]. Imprimir la lista por pantalla

tipos = ["Oro","Basto","Espada","Copa"]
milista = [str(i)+" "+j for j in tipos for i in range(1,13)] 
print(milista)