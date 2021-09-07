Pregunta1=input("¿El dopping positivo de Maradona fue en 1990? ") #No
if Pregunta1=="no" or Pregunta1=="No" or Pregunta1=="NO":
    Pregunta2=input("¿Argentina declaró su independencia en 1810? ") #No
    if Pregunta2=="no" or Pregunta2=="No" or Pregunta1=="NO":
        Pregunta3=input("¿Son 8 las peliculas de Harry Potter? ") #Si
        if Pregunta3=="si" or Pregunta3=="Si" or Pregunta3=="SI":
            print("¡Felicitaciones! Ha ganado el juego.")
        else:
            print("Game Over. Turno del 2° jugador")
    else:
        print("Game Over. Turno del 2° jugador")
else:
    print("Game Over. Turno del 2° jugador")
Pregunta4=input("¿La Ciudad Autonoma de Buenos Aires es la capital de Argentina? ") #Si
if Pregunta4=="si" or Pregunta4=="Si" or Pregunta4=="SI":
    Pregunta5=input("¿Argentina limita con 6 paises? ") #No
    if Pregunta5=="no" or Pregunta5=="No" or Pregunta5=="NO":
        Pregunta6=input("¿Es brasil heptacampeon mundial de futbol? ") #No
        if Pregunta6=="no" or Pregunta6=="No" or Pregunta6=="NO":
            print("¡Felicitaciones! Ha ganado el juego.")
        else:
            print("Game Over. Vuelva a intentarlo")
    else:
        print("Game Over. Vuelva a intentarlo")
else:
    print("Game Over. Vuelva a intentarlo")
    
input()