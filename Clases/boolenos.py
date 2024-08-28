# tipos de datos booleanos
# Los tipos de dato booleano representan uno de dos posibles valores: true o false

valor1 = True #True
valor2= False
print('tipos de valores boleanos:', valor1, valor2)
print('usando type:', type(valor1), type(valor2))

print('usando and', valor1 and valor2)
print('usando or', valor1 or valor2)

# conversiones a boleano
print('entero 0 a boleanos', bool(0))
print('entero 1 a boleanos', bool(1))
print('entero 5 a boleanos', bool(5))
print('entero 7.5 a boleanos', bool(-7.5))

if(5+3-8):
    print('otra vez print')
else:
    print('ya ven')

if (5+3-8*8):
        print('otra vez print')
else:
        print('ya ven')

#conversiones a boleano de strings
print("str '' a boleano", bool('')) # cadena nula: ''
print("str ' ' a boleano", bool(' '))
print("str 'a' a boleano", bool('a'))

print('lista vacia [] a booleano', bool([]))
print('tupla vacia () a booleano', bool(()))
print('diccionario vacio')

      



















