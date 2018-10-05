from models.tipo_pagamento import TipoPagamento

class Boleto(TipoPagamento):
    
    def pagar(self, valor):
        print(f'\nBoleto pago no valor de {valor}')
    