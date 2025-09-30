class Calculo_Numerico:
    def __init__(self, numero):
        self.numero = numero

    def calculo_factorial(self):
        fact = 1
        for i in range(1, self.numero + 1):
            fact *= i
        return fact

    def lista_divisores(self):
        divisores = []
        for i in range(1, self.numero + 1):
            if self.numero % i == 0:
                divisores.append(i)
        return divisores

    def esPrimo(self):
        if self.numero < 2:
            print(f"El número {self.numero} no es primo")
            return False
        for i in range(2, int(self.numero**0.5) + 1):
            if self.numero % i == 0:
                print(f"El número {self.numero} no es primo")
                return False
        print(f"El número {self.numero} es primo")
        return True

    def esPar(self):
        if self.numero % 2 == 0:
            print(f"El número {self.numero} es Par")
            return True
        else:
            print(f"El número {self.numero} es Impar")
            return False


primer_calculo = Calculo_Numerico(5)
print("El factorial del número 5 es:", primer_calculo.calculo_factorial())
print("La lista de divisores del número 5 es:", primer_calculo.lista_divisores())
primer_calculo.esPar()
primer_calculo.esPrimo()
