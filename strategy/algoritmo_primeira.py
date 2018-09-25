from strategy import Strategy

class AlgoritmoPrimeira(Strategy):

  def __str__(self):
    return 'Algoritmo remove do início'

  def pegar_carta_1(self, baralho):
    carta = baralho[0]
    del baralho[0]
    return carta

  def pegar_carta_2(self, baralho):
    carta = baralho[0]
    del baralho[0]
    return carta