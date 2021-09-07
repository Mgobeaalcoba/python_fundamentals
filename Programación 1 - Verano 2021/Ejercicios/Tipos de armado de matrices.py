filas = 3  # Dinámica
columnas = 4
matriz = []
for f in range (filas):
    matriz.append([0]*columnas)
    
print(matriz)

matriz2 =[[0,0,0,0],   #Estática
          [0,0,0,0],
          [0,0,0,0]]

print(matriz2)

filas = 3        #Dinámica usando replicación y listas por comprensión
columndas = 4
matriz3 = [[0]* columnas for i in range (filas)]

print(matriz3)
