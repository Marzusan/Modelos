# Asignadores
# Operadores de aignación, relaiconales y lógicos
# En progrmación , una varible esta formada por un espacio en el
# sistema de alamacenaje y un nombre simbólico que está asociado a dicho espacio.

#Ese espacio contiene una cantidad de información conocida o desconocida, es decir, un valor

variable = 5

# operaodres de asignación
# los operaodres de asignación que se verán en el curso son:
# =, +=, -=, /=, //= (división entera) %=(residuo)  **=

variable += 3.4
# variable = variable + 3.4

variable -= 3.4
variable **=3

# aplicando suma a cadenas
cad1 ='hola'
cad2= 'que have'
print(cad1 +cad2)

cad1 += cad2
print(cad1)

#operadores relacionales
# Los operadores relacionales a considerar son:
# <, >, ==, != (diferente

5> 19
cad1 == 8

# operadores lógicos
# los operadodres lógicos son or, and y not (es la negación)

#expresiones anidadas
# se pueden solucionar empleando las reglas de precedencia:

# primero los paréntesis porque tienen prioridad
# segundo, las expresiones aritméticas por sus porpias reglas
# tercero, las expresiones relacionales
# cuarto, las expresiones lógicas

# controladores de flujo
# se tarta de una estructura de control condicional se cumplen, para decir que acción
# vamos a ejecutar.
#Estas evaluación de condionaes solo puede dar un resultado verdadero o un resultado falso

# sentensia if(si)
# perimite dividir el flujo de un programa en diferentes caminos.
# el if se ejecuta siemore que la expresión que comprueba devuleva true

var1, var2 = 5,2
if 'oración':
    print('caso positivo')
    if var2/var1 < var1:
        print('segundo nivel de if')

# ejeplo de if else
condicional = 5, -16 and False
if condicional:
    print('la condicional es verdadera')
else:
    print('la condicional es falsa')

#ejemplo de if else
n = 78
if n % 2 == 0:
    print(n, 'es un número par')

else:
    print(n, 'es un numero impar')

# tercer comando elif
condic = 32
if condic < 10:
    print('condional es chiquito')
elif condic< 20:
    print('condiocnal no es tan chiquito')

#comando pass
if condic != 0:
    pass





















