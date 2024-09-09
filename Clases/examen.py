# Strigs
# si se puedem hacer multiplicaciones
string2=  'cadena '
10*string2

#Slicing
# Slicing en las cadenas
# El slicing es una capacidad de las cadenas que devuelve un subconjunto o subcadena utilizando dos índices [inicio:fin]:
# El primer índice indica donde empieza la subcadena (se incluye el carácter).
# El segundo índice indica donde acaba la subcadena (se excluye el carácter).

#Inmutabilidad

#Una propiedad de las cadenas es que no se pueden modificar. Si intentamos reasignar un carácter, no nos dejará:

palabra1 = 'palabra'
palabra1[0]
# palabra[0] = "N" erorr

palabra2 = 'pep8'
palabra2[:3] + 'si'
palabra3 = palabra2[:3] + 'si'
palabra3

# Solicitar la entrada del usuario
cadena = input("Introduce una cadena de texto: ")

# Verificar si la longitud de la cadena es mayor o igual a 3 y menor que 10
resultado = len(cadena) >= 3 and len(cadena) < 10

# Mostrar el resultado (True o False)
print(resultado)

a, b = input('Introduce el primer número: '), input('Introduce el segundo número: ')
print('Los dos números son iguales:', a == b)
print('Los dos números son diferentes:', a != b)
print('El primer número {} es mayor que el segundo número {}: {}'.format(a, b, a > b))
print('El segundo número {} es mayor o igual que el primer número {}: {}'.format(b, a, b >= a))
