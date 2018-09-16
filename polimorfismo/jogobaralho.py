import random

class Carta:
    def getNumero(self):
        numeros = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
        return random.choice(numeros)
    
    def getNaipe(self):
        naipe = ('ouro', 'copas', 'espada', 'paus')
        return random.choice(naipe)

    def __init__(self):
        self.numero = self.getNumero()
        self.naipe = self.getNaipe()

    def __str__(self):
        return f'{self.numero} {self.naipe}'

class Baralho:
    def __init__(self):
        self.cartas = []

    def addCartas(self):
        for i in range(52):
            self.cartas.append(Carta())

    def getBaralho(self):
        return self.cartas