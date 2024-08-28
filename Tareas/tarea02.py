# Tarea 2
#Crear un archivo llamado tarea02.py para determinar si los tipos de dato range cumplen:

range2 = range(5)
range3= range(4)

#mutabilidad
range2[2]= 7
#no se puede

#suma
range2 += range3
print('suma', range2)
#no tiene suma

#producto por un entero
range2 *= range3
print('producti', range2)
#no tiene producto


#slicing
print('aplicando slicing', range2(4))
# no tiene slicing


#convertir a lista o tupla
rang4=(4)
print(list(rang4))

#función len
print('aplicando la fucnión len: ', len (rang4))