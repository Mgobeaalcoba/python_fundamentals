Pregunta1=input("¿El dopping positivo de Maradona fue en 1990? ") #No
if Pregunta1=="No":
    Pregunta2=input("¿Argentina declaró su independencia en 1810? ") #No
    if Pregunta2=="No":
        Pregunta3=input("¿Son 8 las peliculas de Harry Potter? ") #Si
        if Pregunta3=="Si":
            Pregunta4=input("¿La Ciudad Autonoma de Buenos Aires es la capital de Argentina? ") #Si
            if Pregunta4=="Si":
                Pregunta5=input("¿Argentina limita con 6 paises? ") #No
                if Pregunta5=="No":
                    Pregunta6=input("¿Es brasil heptacampeon mundial de futbol? ") #No
                    if Pregunta6=="No":
                        Pregunta7=input("¿La raza de perro siberian husky es similar a un lobo? ") #Si
                        if Pregunta7=="Si":
                            Pregunta8=input("¿Elon Musk es el fundador de Tesla? ") #Si
                            if Pregunta8=="Si":
                                Pregunta9=input("¿Son 3 las empresas denominadas como Unicornios argentinos? ") #No
                                if Pregunta9=="No":
                                    print("Felicitaciones. Gano el juego")
else:
    print("Game Over. Se prepara el próximo jugador")
