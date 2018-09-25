from strategy import Strategy
import random

class AlgoritmoRandom(Strategy):

  def __str__(self):
    return 'Algoritmo random'

  def pegar_carta_1(self, baralho):
    return random.choice(baralho)

  def pegar_carta_2(self, baralho):
    return random.choice(baralho)
