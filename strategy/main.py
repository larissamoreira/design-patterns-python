from algoritmo_random import AlgoritmoRandom
from algoritmo_primeira import AlgoritmoPrimeira
from context import Jogo, Baralho, Carta

def main():
  jogo = Jogo(AlgoritmoPrimeira())
  
  for i in range(10):
    c1, c2 = jogo.partida()
    print(c1.get_carta(), c2.get_carta())
  
  print(f'Jogador 1: {jogo.jogador1}, Jogador 2: {jogo.jogador2}')

if __name__ == "__main__":
  main()