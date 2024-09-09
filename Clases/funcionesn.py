# Las funciones
# son fragemntos de código que se peuden ejecutar multiples veces.
# Puede nrecibir y devolver información para comunicarse con el
# proceso principal

#definción y llamada
def saludar():
    print("Hola este print se llama desde la función saludar")

#saludar()

def escibrir_tabla_del_5():
    for i in range(1,11):
        print('5*' , i, '=', 5*i)


#escibrir_tabla_del_5()

#formas de usar el print
val= 10
print('5*', val, '=', 5* val)
print('5*{}={}'.format(10,50))
print('5*{1}={0}'.format(10,50))
print('5*{0}={1}'.format(10,50))
print(f'5*{val}={5*val}')

# Varibales globales vs variables locales
# Una variable declarada en una función no existe en la función principal:

def test(): # todo lo que hagamos en la función se queda en la función
    n= 10

#test()
#print(n) # todo lo que este fuera de las funciones es global y todo lo que esta dentro de las funciones es local

def test1():
    n=20
    print(n)
print('antes de las funciones')
test()
print('después de la función test pero antes de test1')
test1()
print('después de test1')

#return de las funciones

def test():
    n=10
    print('n =', n)
    return n

#m = test_con_return()
# print('globalmente n=', m)

def test_con_multiple_return():
    n=10
    print('localmente n=', n)
    return n, n*5, 6**2 [5,'lobo']

#vals = test_con_multiple_return()
#print(vals, type(vals))

#val1, val2, val3, val4 = test_con_multiple_return()
#print('vals:', val1, val2, val3, val4)

def test_funcion():
    global variable # se hace global
    variable = 10 #variable local
    print(variable)

variable = 20 #variable global
print(variable)
test_funcion()
print(variable)

def test():
    return[1,2,3,4,5]

#variable= test()
#print(variable)
#print('usando slicing:', variable[-2])
#print('usando slicing:', test()[-2])

#Envio de valores
#Para comunicarse con el exterior, las funciones no solo pueden devolver valores,
# también pueden recibir información.

#Parametros y argumentos
# en la definición de una función, los valores que se reciben se denominan parámetros,
# y en la llamada se denominan argumentos.

#def <nombre_de_función> (parametros):
# codigo
#nombre_de_función (argumentos)

def test_funcion(parametro1:int, parametro2: float):
    print(parametro1, parametro2)

argumento1, argumento2 = 5, ['casa']
test_funcion(argumento1, argumento2)

#argumentos por posición
# Trabajdno por argumentos y parámetros

def funcion1(a, b):
    print(a-b)

funcion1(25,7) # funcion1(b=25,a=7)

x,y= 25,7

def funcion_resta(a=25, b=7):
    print(a-b)

funcion_resta(a=50, b=10)















