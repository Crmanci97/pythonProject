def determinar_par_o_impar(numero):

    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

numero = int(input("Ingrese un número entero: "))

resultado = determinar_par_o_impar(numero)
print("El número", numero, "es : ", resultado)