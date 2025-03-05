#Herencia, Polimorfismo

class Numeros:
    def __init__(self, n):
        self.n = n

    def print_numeros(self):
        for i in range(self.n):
            if ((self.n % 2) == 0):
                print("El número es: ", i)
            else:
                print("El cuadrado del número es: ", i * i)

class Racionales(Numeros):
    def __init__(self, n):
        super().__init__(n)

    def print_numeros(self):
        #as_integer_ratio()
        print("El número racional es: ", self.n)
        print("El número racional en forma de fracción es: ", self.n.as_integer_ratio())
    
    def print_hello(self):
        return "Hello Edgar"