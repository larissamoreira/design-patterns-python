from abc import ABC, abstractmethod

class Strategy(ABC):

  @abstractmethod
  def pegar_carta_1(self):
    pass

  @abstractmethod
  def pegar_carta_2(self):
    pass