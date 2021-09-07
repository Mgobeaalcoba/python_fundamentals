# Toma una entrada n y saca los números de 1 a n. Por cada multiplo de 3, imprime "Solo" en lugar del número. Por cada multiplo
# de 5 imprime "Learn" en lugar del numero. Para los numeros que son multiplos de 3 y 5 imprime "SoloLearn".

def imprimirlista(lista):
    largo=len(lista)
    for i in range(largo):
        print(lista[i],end=" ")
    print()

n=int(input("Ingrese un numero positivo: "))
lista=[]
for i in range(1,n):
    lista.append(i)
    
imprimirlista(lista)

for i in range(len(lista)):
    if lista[i]%3==0 and lista[i]%5==0:
        lista[i]="SoloLearn"
    elif lista[i]%3==0:
        lista[i]="Solo"
    elif lista[i]%5==0:
        lista[i]="Learn"

imprimirlista(lista)
    