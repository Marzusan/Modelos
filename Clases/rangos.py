# rangos
# la función range() retorna una sucesión de números en un rango, range(start, stop, step)

rango1 =range(5)
print('ejemplo de rango:', rango1, 'rango es de tipo', type(rango1))


#conversion de range a lista
print('convirtiendo el rango a lista:', list(rango1)) # para verlos

rango2 = range(3, 102, 3)
print('convirtiendo el rango a lista:', list(rango2))

print('aplicando el slicing al rango', list(rango2[2:5]))


