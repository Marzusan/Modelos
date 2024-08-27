# diccionario{}
# los diccionarios son usados para almacenar datos en formatos key: value
diccionario1 =dict()
print('ej de diccionario:', diccionario1, 'su tipo es:', type(diccionario1))

diccioanrio1= {'llave1':'lobo', 'llave2': -82.654, 34: 'cosa','llave4': [2,3,4]}

#slicing a diccionarios
print('para el slicing uso la llave')
print(diccionario1['llave2'])
print('usando len, el diccionario tiene: ', len(diccionario1), 'elementos')

#Sets
# Los conjuntos son una coleccion de valores no ordenados que no admiten duplicados
# entre { } y separados con comas
set1 = { 3,6,'azul'}
print('Ej de conjunto:', set1, 'de tipo: ', type(set1))

set={3, 'jajav', 8, 12, 8, 'jaja','jejej', 3, 12}
print('ej de conjunto:', set1)

print(list(set1))
print('index de un set', set1[0])









