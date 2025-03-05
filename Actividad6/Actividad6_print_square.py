print("Hola Edgar, ingresa un número entero")
try:
    n = int(input())
    print("El número ingresado es", n)

    for i in range(n):
        if ((n % 2) == 0):
            print("El número es: ", i)
        else:
            print("El cuadrado del número es: ", i * i)
except:
    print("La entrada no es un entero")