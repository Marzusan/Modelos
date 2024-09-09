# Crear un archivo llamado tarea04.py que resuelva los siguientes ejercicios:

# Considera las siguientes calificaciones:

calif_1 = 10

calif_2 = 7

calif_3 = 4

# Calcula el promedio de las calificaciones considerando que:

# La primera nota vale un 15% del total
# La segunda nota vale un 35% del total
# La tercera nota vale un 50% del total

promedio= ((calif_1*15)/100) + ((calif_2*35)/100) + ((calif_3*50)/100)
print(promedio)


# La siguiente matriz debe cumplir que el 4to valor de cada fila debe ser igual a la suma de los primeros 3 valores.
# Crea un código para hacer las correcciones necesarias

matriz = [ [1, 1, 1, 3],
           [2, 2, 2, 7],
           [3, 3, 3, 9],
           [4, 4, 4, 13] ]

matriz[0][3] = matriz[0][0]+ matriz[0][1] + matriz[0][2] + matriz[0][3]
matriz[1][3] = matriz[1][0]+ matriz[1][1] + matriz[1][2] + matriz[1][3]
matriz[2][3] = matriz[2][0]+ matriz[2][1] + matriz[2][2] + matriz[2][3]
matriz[3][3] = matriz[3][0]+ matriz[3][1] + matriz[3][2] + matriz[3][3]

print(matriz)

fila=0

for fila in range (4):
        matriz[fila][3] != sum(matriz[fila][:3])
        matriz[fila][3] = sum(matriz[fila][:3])
        print('se modificó', fila)
else:
        print('no se modifico', fila)








