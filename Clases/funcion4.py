# Giving a string, create 2 f

#def metodo1(palabra: str) ->int:
 #   numero_espacios = 0
  #  for letra in palabra:
   #     if letra == ' ':
    #        numero_espacios += 1
     #       return numero_espacios

#def metodo2(palabra:str)
   # numero_espacios = palabra.count (' ')
   # print(f' 'la farse tiene)


# given a list, create a funcion to print the odd numbers in the list
    #def imprimir_impares(listas: list):
     #for numero in lista:
      # if numero % 2== 1
        # print(numero, end= ' ')

#funciones recurssivas

def factorial(valor:int) -> int:
    if valor < 0:
        print('No existe el factorial de un número negativo')
    return
    resultado = 1
    for i in range(2, valor+1):
     resultado += 1
     return resultado


def factorial(valor: int) -> int:
    if valor < 0:
        print('No existe el factorial de un número negativo')
        return None  # Indicamos que no hay un resultado válido
    elif valor == 0 or valor == 1:
        return 1  # Caso base
    else:
        return valor * factorial(valor - 1)




#