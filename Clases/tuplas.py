# Tuplas

# Colección de elemetos distintos ordenados  separados entre ()  y separados por comas.

tupla = (3,2, 'ocho')
print('la tupla:', tupla, 'es tipo:', type(tupla))

# como caracteristicas principal de las tuplas, cuando tenemos una tupla con 1 elemento
tupla1 =(5)
print('La tupla de 1 elemento es: ', tupla1, 'es de tipo:', type(tupla1))

# verdadera una forma de definir una tupla con 1 elemento
tupla1 =('5',)
print('su cantidad de elementos es: ', len(tupla1))

#slicing
tupla3= (3,6, 'ocho', 'lobo', 'chocolate', 'tieraa', '[9,2]', 'cosa')
print('tupla3', tupla3)
print('aplicando slicing', tupla[4])
print('aplicando slicing con num negativos', tupla[-4:-1])

#mutabilidad , no tiene esas caracteristicas de remplazar los valores
tupla[3] = 'cachorro'

#suma de tublas
tupla4 =(4,5,6,7,8),
tupla1+ tupla3
print('aplicando la fucnión len: ', len (tupla1+ tupla3))
print('multiplicando tuplas por un entero: ', tupla4*3)

#convertiendo tuplas a listas
print('convertiendo tuplas a listas ', list(tupla1), 'tiene tipo:'
      , type(list(tupla1)))

#converir listas a  tuplas
print('convertiendo listas a tuplas ',tuple(['azul', 'soso']))

# a manera de resumen
#mutabilidad
#operaciones con tuplas: suma, productos por un entero
#slicing
#convirtiendo duplas a listas





