from strategy import Strategy
import random

class AlgoritmoRandom(Strategy):

  def pegar_carta_1(self, baralho):
    return random.choice(baralho)

  def pegar_carta_2(self, baralho):
    return random.choice(baralho)
