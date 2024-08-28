# Crear un diccionario de ejemplo
diccionarioc = {
    'canciones': 'bad boy, free fall',
    'artistas': 'rainbow kitten, ''bad bonny',
    'reproducciones': 100000
}

# 1. Método `get()`
valor_canciones = diccionarioc.get('canciones')
print('las canciones son', valor_canciones)

# 2. Método `keys()`
llaves = diccionarioc.keys()
print("Las llaves del diccionario son:", list(llaves))

# 3. Método `values()`
valores = diccionarioc.values()
print("Los valores del diccionario son:", list(valores))

# 4. Método `items()`
elemen = diccionarioc.items()
print("Los elementos (pares clave-valor) del diccionario son:")
for clave, valor in elemen:
    print(f"{clave}: {valor}")

# 5. Método `update()`
diccionarioc.update({'profesion': 'Ingeniera'})
print("\nUso de update():")
print("Diccionario después de update():", diccionarioc)

# 6. Método `pop()`
valor_artista = diccionarioc.pop('artistas')
print("\nUso de pop():")
print(f"Se ha eliminado la ciudad, que tenía el valor: {valor_artista}")
print("Diccionario después de pop():", diccionarioc)

# 7. Método `popitem()`
clave_valor = diccionarioc.popitem()
print("\nUso de popitem():")
print(f"Se ha eliminado el par clave-valor: {clave_valor}")
print("Diccionario después de popitem():", diccionarioc)

# 8. Método `clear()`
diccionarioc.clear()
print("Diccionario después de clear():", diccionarioc)