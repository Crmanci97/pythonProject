def encontrar_maximo_minimo(lista):

    if not lista:
        return None, None

    maximo = minimo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero

    return maximo, minimo

numeros = [5, 8, 3, 1, 9, 6, 2, 7, 4]
maximo, minimo = encontrar_maximo_minimo(numeros)
print("El número más grande en la lista es :", maximo)
print("El número más pequeño en la lista es :", minimo)