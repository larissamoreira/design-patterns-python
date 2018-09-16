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
        for i in range(5):
            self.cartas.append(Carta())

    def getCarta(self):
        return random.choice(self.cartas)

class Jogo:
    def __init__(self):
        self.jogador1 = Baralho()
        self.jogador2 = Baralho()
        self.jogador1.addCartas()
        self.jogador2.addCartas()
        self.rodada = 0

    def partida(self):
        carta_j1 = self.jogador1.getCarta()
        carta_j2 = self.jogador2.getCarta()
        
        print(f'Rodada [{self.rodada}]')
        print(f'Jogador 1: {carta_j1}')
        print(f'Jogador 2: {carta_j2}')
    
    def start(self):
        while(self.rodada < 10):
            self.partida()
            self.rodada = self.rodada + 1
        
jogo1 = Jogo()
jogo1.start()
