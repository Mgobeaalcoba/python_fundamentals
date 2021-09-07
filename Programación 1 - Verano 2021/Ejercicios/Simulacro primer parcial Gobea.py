# Programa que genere una lista por comprensión con los numeros entre 1 y N que sean multiplos de 7 o que terminen en 7. Mostrar
# por pantalla la lista obtenida. N se ingresa por teclado

def lista_comprension(N):
    lista=[n for n in range(1,N+1) if n%7==0 or str(n)[-1]=="7"]
    return lista
    
def lista_comprension2(N):
    lista=[n for n in range(1,N+1) if n%7==0 or n%10==7]
    return lista
    
# Programa principal:
n=int(input("Ingrese un numero natural que será el máximo de su lista: "))
milista=lista_comprension2(n)
print(milista)