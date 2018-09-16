import random
numeros = {'A': 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 11, 'Q': 12, 'K': 13}
naipes = {'ouro': 1, 'copas': 2, 'espada': 3, 'paus': 4}

class Carta:
    def makeNumero(self):
        return random.choice(list(numeros.keys()))

    def makeNaipe(self):
        return random.choice(list(naipes.keys()))

    def pontoNaipe(self, naipe):
        return naipes[naipe]

    def pontoNumero(self, numero):
        return numeros[numero]

    def __init__(self):
        self.numero = self.makeNumero()
        self.naipe = self.makeNaipe()

    def getCarta(self):
        return f'{self.numero} {self.naipe}'

class Baralho:
    def __init__(self):
        self.cartas = []

    def addCartas(self):
        for i in range(5):
            self.cartas.append(Carta())

    def getRandomCarta(self):
        return random.choice(self.cartas)

    def getBaralho(self):
        return self.cartas

class Jogo:
    def __init__(self):
        self.b = Baralho()
        self.b.addCartas()
        self.jogador1 = 0
        self.jogador2 = 0
        self.rodada = 0

    def addPontosJogador1(self, numero, naipe):
        self.jogador1 += numero + naipe
        return f'{self.jogador1}'

    def addPontosJogador2(self, numero, naipe):
        self.jogador2 += numero + naipe
        return f'{self.jogador2}'
    
    def partida(self):
        c1 = self.b.getRandomCarta() #jogador 1
        c2 = self.b.getRandomCarta() #jogador 2

        # Pontos J1
        p1_naipe = c1.pontoNaipe(c1.naipe)
        p1_numero = c1.pontoNumero(c1.numero)

        # Pontos J2
        p2_naipe = c2.pontoNaipe(c2.naipe)
        p2_numero = c2.pontoNumero(c2.numero)

        print(f'Rodada [{self.rodada}]')
        print('------------------------------------------------------')
        print(f'Jogador 1: {c1.numero} = {p1_numero} | {c1.naipe} = {p1_naipe} | pontuação atual: {self.addPontosJogador1(p1_numero, p1_naipe)}')
        print(f'Jogador 2: {c2.numero} = {p2_numero} | {c2.naipe} = {p2_naipe} | pontuação atual: {self.addPontosJogador2(p2_numero, p2_naipe)}')
        print()

    def start(self):
        while(self.rodada < 4):
            self.partida()
            self.rodada = self.rodada + 1
        print(f'Pontuação final jogador 1: {self.jogador1}')
        print(f'Pontuação final jogador 2: {self.jogador2}')
        print()
        if self.jogador1 > self.jogador2:
            print(f'O vencedor é o jogador 1 com {self.jogador1} pontos!')
        else:
            print(f'O vencedor é o jogador 2 com {self.jogador2} pontos!')
        
jogo1 = Jogo()
jogo1.start()

"""
    def pontoCarta(self, **kwargs):
        for key, value in kwargs.items():
            print(key,value)
"""