# write your code here
# Calculate the factorial of a number (a non-negative integer)

def factorial(n):
    value = 1
    if n > 1:
        for i in range(1, n+1):
            value *= i
    return value

factorial(35)

#Ask for 3 numbers, check if the third number is in the range of the 2 first numbers
# write your code here
lim_1, lim_2 = float(input('Introduce un límite: ')), float(input('Introduce otro límite: '))
value = float(input('Introduce un valor: '))

lim_inf, lim_sup = min(lim_1, lim_2), max(lim_1, lim_2)
if lim_inf <= value <= lim_sup:
    print('El valor sí está en el rango')
else:
    print('El valor no está en el rango')

#Given a string, 2 methods to count the spaces in the string
# write your code here
string = input('Introduce una cadena: ')

# Method 1. With loop
num_spaces = 0
for letter in string:
    if letter == ' ':
        num_spaces += 1
print('Método 1. El número de espacioes es ', num_spaces)
# Method 1. With count
print('Método 2. El número de espacioes es ', string.count(' '))

#Given a list, ask for two indexes of the list, interchange those values
# write your code here
given_list = [4, 7, 'azul', 'loza', ['a', 'b', 'c']]
print('La lista original es: ', given_list)

idx1, idx2 = int(input('Dar el 1er índice: ')), int(input('Dar el 2do índice: '))
#Intercambiar valores
given_list[idx1], given_list[idx2] = given_list[idx2], given_list[idx1]

print('La lista modificada es: ', given_list)

#Given a list, 2 methods to find the length of the list
# write your code here
given_list = [4, 7, 'azul', 'loza', ['a', 'b', 'c']]

# Method 1. With loop
for idx, elt in enumerate(given_list):
    pass

print('Método 1. La longitud de la lista es: ', idx + 1)
print('Método 2. La longitud de la lista es: ', len(given_list))

#Given a dictionary, sort the dictionary by key
# write your code here
given_dict = {'z': 10, 'p': 9, 'azul': 'color', 'a': -3.2}

# get keys
keys = list(given_dict.keys())
# sort keys
keys.sort()
# create the new dictionary
new_dict = {}
for key in keys:
    new_dict[key] = given_dict[key]

print(new_dict)

#Given a dictionary, find the sum of all values
# write your code here
given_dict = {'z': 10, 'p': 9, 'azul': 29, 258: -3.2}

# get values
values = list(given_dict.values())
print('La suma de los valores es: ', sum(values))

#Given a list of integers, print the even numbers
# write your code here
given_list = [5, 23, 8, 12, -8, -62, -0, [2, 3, 4]]

for value in given_list:
    if value % 2 == 0:
        print(value)



# Ejercicio
"""
2) Recibe por teclado un número entero  𝑛  e imprime '123...n'

Ejemplo:

𝑛=5
  devuelve '12345'

Restricciones:

1≤𝑛≤150
"""
numero_str = input('Introduce un número del 1 al 150: ')
n = int(numero_str)

print(list(range(1, n+1)))

# Bucle que continúa hasta que se introduce un número impar
while True:
    try:
        # Solicitar entrada al usuario
        numero = int(input("Introduce un número impar: "))

        # Verificar si el número es impar
        if numero % 2 != 0:
            print("¡Correcto! Has introducido un número impar.")
            break
        else:
            print("El número es par. Inténtalo de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número.")

# # Sumar todos los números enteros pares desde 0 hasta 100
# suma_pares = sum(range(0, 101, 2))
#
# # Mostrar el resultado
# print(f"La suma de todos los números pares desde 0 hasta 100 es: {suma_pares}")

# Solicitar al usuario la cantidad de números que desea introducir
cantidad = int(input("¿Cuántos números deseas introducir?: "))

# Inicializar una lista para almacenar los números
numeros = []

# Bucle para solicitar los números al usuario
for i in range(cantidad):
    numero = float(input(f"Introduce el número {i+1}: "))
    numeros.append(numero)

# Calcular la media aritmética
if cantidad > 0:
    media = sum(numeros) / cantidad
    print(f"La media aritmética de los números introducidos es: {media}")
else:
    print("No has introducido ningún número.")

 Todos los números del 0 al 10
lista_0_10 = list(range(0, 11))

# Todos los números del -10 al 0
lista_neg10_0 = list(range(-10, 1))

# Todos los números pares del 0 al 20
lista_pares_0_20 = list(range(0, 21, 2))

# Todos los números impares entre -20 y 0
lista_impares_neg20_0 = list(range(-19, 0, 2))

# Todos los números múltiplos de 5 del 0 al 50
lista_multiplos_5 = list(range(0, 51, 5))

# Imprimir las listas
print("Todos los números del 0 al 10:", lista_0_10)
print("Todos los números del -10 al 0:", lista_neg10_0)
print("Todos los números pares del 0 al 20:", lista_pares_0_20)
print("Todos los números impares entre -20 y 0:", lista_impares_neg20_0)
print("Todos los números múltiplos de 5 del 0 al 50:", lista_multiplos_5)

# Solicitar un número entero al usuario
n = int(input("Introduce un número entero: "))

# Realizar las acciones condicionales
if n % 2 != 0:
    print("Raro")
elif n % 2 == 0 and 2 <= n <= 5:
    print("No es raro")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Raro")
elif n % 2 == 0 and n > 20:
    print("No es raro")

# Solicitar un número entero al usuario
n = int(input("Introduce un número entero: "))

# Imprimir el cuadrado de todos los enteros menores que n
for i in range(n):
    print(i**2)

# Definir la función que calcula el n-ésimo término de la serie de Fibonacci
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Solicitar al usuario el número n
n = int(input("Introduce un número entero n para calcular el término n-ésimo de la serie de Fibonacci: "))

# Calcular el enésimo término de la serie de Fibonacci y mostrarlo
resultado = fibonacci(n)
print(f"El término {n}-ésimo de la serie de Fibonacci es: {resultado}")

# Definir la función que calcula el n-ésimo término de la serie de Fibonacci
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Solicitar al usuario el número n
n = int(input("Introduce un número entero n para imprimir los primeros n términos de la serie de Fibonacci: "))

# Imprimir los primeros n términos de la serie de Fibonacci
print(f"Los primeros {n} términos de la serie de Fibonacci son:")
for i in range(1, n+1):
    print(fibonacci(i))


def cortar_bastones(bastones):
    resultados = []

    while bastones:
        # Contamos cuántos bastones hay
        resultados.append(len(bastones))

        # Encontramos la longitud mínima de los bastones
        min_longitud = min(bastones)

        # Eliminamos las piezas más cortas
        bastones = [bastón - min_longitud for bastón in bastones if bastón > min_longitud]

    return resultados


# Ejemplo de uso
bastones = [5, 4, 4, 2, 2, 8]
print(cortar_bastones(bastones))

def contar_cuadrados_en_rango(a, b):
    count = 0
    # Itera sobre posibles valores de n donde n^2 está en el rango [a, b]
    n = 1
    while n * n <= b:
        if n * n >= a:
            count += 1
        n += 1
    return count

# Ejemplo de uso
a = 10
b = 50
print(contar_cuadrados_en_rango(a, b))  # Salida: 5
