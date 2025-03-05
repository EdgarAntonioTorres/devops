class Numeros:
    def __init__(self, n):
        self.n = n

    def print_numbers(self):
        for i in range(n):
            if ((n % 2) == 0):
                print("El número es: ", i)
            else:
                print("El cuadrado del número es: ", i * i)

print("Hola Edgar, ingresa un número entero")
try:
    n = int(input())
    entero = Numeros(n)
    entero.print_numbers()
except:
    print("La entrada no es un entero")