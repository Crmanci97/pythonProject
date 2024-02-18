def convierte_fahrenheit_a_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Ejemplo de uso:
temperatura_fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
temperatura_celsius = convierte_fahrenheit_a_celsius(temperatura_fahrenheit)
print("La temperatura equivalente en grados Celsius es :", temperatura_celsius)