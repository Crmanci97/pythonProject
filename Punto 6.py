def suma_lista(lista):

    suma = 0
    for numero in lista:
        suma += numero
    return suma

numeros = [1, 2, 3, 4, 5]
resultado = suma_lista(numeros)
print("La suma de los números en la lista es :", resultado)