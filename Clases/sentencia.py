# sentencia for (para) con listas

numeros =[1,2,3,4,4,5]
#for idx in numeros: #para[variable local] en [lista]
    #coódigo para ser realizado en el for
#print(idx)

#ejemplos
promedio= 0
numeros= [0,2,4,5,6,8]

for idx in numeros:
    promedio += idx
    print(str(idx))

promedio /= len(numeros)
print('el promedio es:', promedio)

# ejemplo 3:
numeros2= [0,2,4,5,6,8]
dosito = 0
for hola in numeros2:
    dosito += 1
    print('se está ejecutando el for')
    print('la longuitud de la litas es', dosito)


#uso de continue y break

 #for jaja in range(2, 18):
   #print(jaja)
   #if jaja %2 == 0:
      # print('es par')
      # continue
       #print('mas código')
# else:
 #print('es impar')

 for letra in 'palabra':
     print(letra)



