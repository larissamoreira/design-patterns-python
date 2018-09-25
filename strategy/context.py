import random
from random import shuffle

numeros = {'A': 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 11, 'Q': 12, 'K': 13}
naipes = {'ouro': 1, 'copas': 2, 'espada': 3, 'paus': 4}

class Carta:
    def __init__(self, naipe, numero):
        self.__numero = numero
        self.__naipe = naipe

    def ponto_naipe(self, naipe):
        return naipes[naipe]

    def ponto_numero(self, numero):
        return numeros[numero]
    
    @property
    def numero(self):
        return self.__numero

    @property
    def naipe(self):
        return self.__naipe

    def get_carta(self):
        return f'{self.numero} {self.naipe}'

class Baralho:
    def __init__(self):
        self.cartas = []

    def add_cartas(self):
        for naipe in naipes.keys():
            for numero in numeros.keys():
                self.cartas.append(Carta(naipe, numero))

    def embaralhar(self):
        shuffle(self.cartas)
    
    def get_baralho(self):
        return self.cartas

class Jogo:
    def __init__(self, strategy):
        self.__baralho = Baralho()
        self.__baralho.add_cartas()
        self.__baralho.embaralhar()
        self.__jogador1 = 0
        self.__jogador2 = 0
        self.__rodada = 0
        self.__strategy = strategy

    @property
    def baralho(self):
        return self.__baralho
    
    @property
    def jogador1(self):
        return self.__jogador1

    @property
    def jogador2(self):
        return self.__jogador2
    
    @property
    def strategy(self):
        return self.__strategy
    
    @property
    def rodada(self):
        return self.__rodada

    @rodada.setter
    def rodada(self, new_rodada):
        self.__rodada = new_rodada
      
    @jogador1.setter
    def jogador1(self, new_jogador1):
        self.__jogador1 = new_jogador1

    @jogador2.setter
    def jogador2(self, new_jogador2):
        self.__jogador2 = new_jogador2

    @strategy.setter
    def strategy(self, new_strategy):
        self.__strategy = new_strategy
        
    def add_pontos_jogador1(self, numero, naipe):
        self.jogador1 += numero + naipe
        return self.jogador1

    def add_pontos_jogador2(self, numero, naipe):
        self.jogador2 += numero + naipe
        return self.jogador2

    def partida(self):
        self.rodada = self.rodada + 1

        c1 = self.strategy.pegar_carta_1(self.baralho.get_baralho())
        c2 = self.strategy.pegar_carta_2(self.baralho.get_baralho())

        self.add_pontos_jogador1(c1.ponto_numero(c1.numero), c1.ponto_naipe(c1.naipe))
        self.add_pontos_jogador2(c2.ponto_numero(c2.numero), c2.ponto_naipe(c2.naipe))

        return c1, c2
