 # Comando para las listas

elaestehik = ['e-girl','indie','edgy','fairy', 'indie']

# list.append(x), solo agregas un elemento
elaestehik.append('academia')
print(elaestehik)

# list.extend(iterable), agregas más de un elemento
elaestehik.extend(['grunge','goth','emo' ])
print(elaestehik)

# list.insert(i, x)  insertas un objeto a la lista
elaestehik.insert(2,4)
print(elaestehik)

# list.remove(x) quitas un elemento
elaestehik.remove('edgy')
print(elaestehik)

# list.pop([i]) quitas un elemento pero con la posición
elaestehik.pop(3)
print(elaestehik)

# list.clear(), quita toda la lista

# list.index(x[, start[, end]]), en que posición esta un elemento
elaestehik.index('e-girl')
print(elaestehik.index('e-girl'))

# list.count(x)
elaestehik.count('indie')
print(elaestehik.count('indie'))

# list.sort(*, key=None, reverse=False)

# list.reverse()
elaestehik.reverse()
print(elaestehik)

#  list.copy()
aes2 = list.copy()
print(elaestehik)