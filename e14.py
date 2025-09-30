class Carta:
    def __init__(self, rango, simbolo):
        self.rango = rango
        self.simbolo = simbolo

    def __eq__(self, otra):
        return self.rango == otra.rango and self.simbolo == otra.simbolo

    def __lt__(self, otra):
        return self.rango < otra.rango

    def __str__(self):
        return f"La carta tiene rango {self.rango} y símbolo {self.simbolo}"


signos = [chr(9824), chr(9825), chr(9826), chr(9827)]
rangos = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,
          "J":11,"Q":12,"K":13,"A":14}

trebol_1_rango_1 = (signos[3], rangos["8"])
corazon_2_rango_2 = (signos[1], rangos["3"])
pica_3_rango_3 = (signos[0], rangos["8"])

carta_1 = Carta(trebol_1_rango_1[1], trebol_1_rango_1[0])
carta_2 = Carta(corazon_2_rango_2[1], corazon_2_rango_2[0])
carta_3 = Carta(pica_3_rango_3[1], pica_3_rango_3[0])

print(carta_1)
print(carta_2)
print(carta_3)
print(carta_1 > carta_2)
print(carta_1 == carta_2)
