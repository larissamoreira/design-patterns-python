from models.tipo_pagamento import TipoPagamento

class CartaoCredito(TipoPagamento):
    
    def pagar(self, valor):
        print(f'\nTransação aprovada no valor de {valor}')
    