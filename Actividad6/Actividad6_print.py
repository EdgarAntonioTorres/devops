print("Hola Edgar, ingresa un número entero")
try:
    n = int(input())
    print("El número ingresado es", n)

    for i in range(n):
        print(i)
except:
    print("La entrada no es un entero")