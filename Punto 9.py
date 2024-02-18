import random

def generar_matriz(filas, columnas, rango_inicio, rango_fin):

    matriz = [[random.randint(rango_inicio, rango_fin) for _ in range(columnas)] for _ in range(filas)]
    return matriz

def imprimir_matriz(matriz):

    for fila in matriz:
        print(" ".join(map(str, fila)))

filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))
rango_inicio = int(input("Ingrese el valor mínimo para los números aleatorios: "))
rango_fin = int(input("Ingrese el valor máximo para los números aleatorios: "))

matriz = generar_matriz(filas, columnas, rango_inicio, rango_fin)
print("Matriz generada:")
imprimir_matriz(matriz)