# función while
#iteraciones
# iterar significa realizar una acción varias veces
# Cada vez que se repite se denomina iteración

#Controlador o sentencia while (mientras)
# se basa en repetir un bloque a partir de evaluar una condición lógica

#Queda en las manos del programador decidir el momento en que la condición
# cambie o False para hacer que el while finalice

lista = [ 'chocolate', 'tristeza', 'cualquiera', 'naranjas', 'azul', 'parque']
indice = -3
while lista[indice] != 'cualquiera':
    print(indice, lista[indice])
    indice += 1
else:
    print('se cumplió la condición, ya me quiero mimir')

#ejemplo donde no se cumple la condición de paro
#idx= 0
#while True:
    #idx *= 2
    #print( idx)
#else:
    #print('salio')

#ejemplo de brake
c= 0
while c <= 5:
    print(" c vale", c)
    c+= 1
    if c== 4:
        print( "rompemos el bucle cuando c vale", c)
        continue

else:
    print("se ha completado todo la interación y c vale", c)


