print("Calcular Áreas de figuras Geométricas.\n")
print("/1. Cuadrado. /2. Circulo. /3. Triángulo.    /4. Trapecio.   /5. Rectángulo." )
x = int(input("Escoja un número : "))

if x == 1:
    L = int(input("Ingrese el valor del lado : "))
    area_cuadrado = L ** 2
    print("El área del cuadrado es :", area_cuadrado)

elif x == 2:
    r = int(input("Ingrese el radio : "))
    area_circulo = 3.1416 * r ** 2
    print("El área del círculo es :", area_circulo)

elif x == 3:
    b = int(input("Ingrese la base : "))
    h = int(input("Ingrese la altura : "))
    area_triangulo = b * h / 2
    print("El área del triángulo es : ", area_triangulo)

elif x == 4:
    b1 = int(input("Ingrese la base 1 : "))
    b2 = int(input("Ingrese la base 2 : "))
    h = int(input("Ingrese la altura : "))
    area_trapecio = (b1 + b2) * h / 2
    print("El área del trapecio es :", area_trapecio)

elif x == 5:
    b = int(input("Ingrese la base : "))
    h = int(input("Ingrese la altura : "))
    area = b * h
    print("El área del rectángulo es :", area)

else:
    print("Opción no válida. Por favor, elija un número del 1 al 5.")




