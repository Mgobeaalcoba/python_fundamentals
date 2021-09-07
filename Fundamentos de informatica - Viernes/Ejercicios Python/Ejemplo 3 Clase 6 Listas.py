# Primera parte

ELEMENTOS = 50
v = []
i = 0
suma = 0
while i < ELEMENTOS:
    n = int(input("Ingrese un numero: "))
    v.append(n)
    suma = suma + n
    i = i + 1
prom = suma / ELEMENTOS
print("El promedio es:",prom)

# Segunda parte - Imprimir mayores

i = 0
while i < ELEMENTOS:
    if v[i] > prom:
        print(v[i])
    i = i + 1
    
