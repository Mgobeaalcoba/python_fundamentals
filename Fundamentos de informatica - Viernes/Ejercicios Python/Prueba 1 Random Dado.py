import random

def lanzardado():
    return random.randint(1,6) # random arroja un numero al azar y randint fija un rango para ese numero. ej 1 y 6 para el dado

#Programa
dado = lanzardado()
print(dado)
