from abc import ABC, abstractmethod

class TipoPagamento(ABC):

    @abstractmethod
    def pagar(self, valor):
        pass
    