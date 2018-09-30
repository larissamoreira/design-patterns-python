from tipo_pagamento import TipoPagamento

class CartaoCredito(TipoPagamento):
    
    def pagar(self, valor):
        print(f'Transação aprovada no valor de {valor}')
    