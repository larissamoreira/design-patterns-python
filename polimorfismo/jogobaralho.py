import random
from random import shuffle
#from abc import ABC, abstractmethod

numeros = {'A': 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 11, 'Q': 12, 'K': 13}
naipes = {'ouro': 1, 'copas': 2, 'espada': 3, 'paus': 4}

class Carta:
    def __init__(self, naipe, numero):
        self.numero = numero
        self.naipe = naipe

    def ponto_naipe(self, naipe):
        return naipes[naipe]

    def ponto_numero(self, numero):
        return numeros[numero]

    def __str__(self):
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
    
    def carta_fim(self):
        return self.cartas.pop()
    
    def carta_aleatoria(self):
        return random.choice(self.cartas)

    def carta_inicio(self):
        return self.cartas[0]
    
    def get_baralho(self):
        return self.cartas

class Jogo:
    def __init__(self):
        self.baralho = Baralho()
        self.baralho.add_cartas()
        self.baralho.embaralhar()
        self.jogador1 = 0
        self.jogador2 = 0
        self.rodada = 0

    def add_pontos_jogador1(self, numero, naipe):
        self.jogador1 += numero + naipe
        return self.jogador1

    def add_pontos_jogador2(self, numero, naipe):
        self.jogador2 += numero + naipe
        return self.jogador2
    
    def retirar_carta(self):
        retirada = []
        retirada.append(self.baralho.carta_aleatoria())
        retirada.append(self.baralho.carta_aleatoria())
        return retirada
    
    def partida(self):
        retiradas = self.retirar_carta()
        c1 = retiradas[0]
        c2 = retiradas[1]

        self.add_pontos_jogador1(c1.ponto_numero(c1.numero), c1.ponto_naipe(c1.naipe))
        self.add_pontos_jogador2(c2.ponto_numero(c2.numero), c2.ponto_naipe(c2.naipe))

    def start(self):
        while(self.rodada < 10):
            self.partida()
            self.rodada = self.rodada + 1
        print(f'Pontuação final jogador 1: {self.jogador1}')
        print(f'Pontuação final jogador 2: {self.jogador2}')
        print()
        if self.jogador1 == self.jogador2:
            self.partida()
            self.rodada = self.rodada + 1
        print(f'Partidas: {self.rodada}')
        if self.jogador1 > self.jogador2:
            print(f'O vencedor é o jogador 1 com {self.jogador1} pontos!')
        else:
            print(f'O vencedor é o jogador 2 com {self.jogador2} pontos!')

class JogoRetirarFim(Jogo):
    def retirar_carta(self):
        retirada = []
        retirada.append(self.baralho.carta_fim())
        retirada.append(self.baralho.carta_fim())
        return retirada
        
jogo1 = JogoExtendido()
jogo1.start()