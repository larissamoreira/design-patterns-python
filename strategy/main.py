from algoritmo_random import AlgoritmoRandom
from algoritmo_primeira import AlgoritmoPrimeira
from context import Jogo, Baralho, Carta

def main():
  jogo = Jogo(AlgoritmoPrimeira())
  continuar = True
  
  while(continuar and jogo.rodada < 10):
    c1, c2 = jogo.partida()
    print('---------------------')
    print(f'Rodada: {jogo.rodada}\n{jogo.strategy}\nCartas: {c1.get_carta()} - {c2.get_carta()}')
    print('---------------------')
    print('Continuar jogo [0]\nMudar algoritmo [1-Random, 2-Remove do início]\n')
    jogar = int(input('Opção: '))
    if jogar == 0:
      continuar = True
    elif jogar == 1:
      jogo.strategy = AlgoritmoRandom()
    elif jogar == 2:
      jogo.strategy = AlgoritmoPrimeira()

  
  print(f'Jogador 1: {jogo.jogador1}, Jogador 2: {jogo.jogador2}')

if __name__ == "__main__":
  main()